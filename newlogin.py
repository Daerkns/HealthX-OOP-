import bcrypt


class AccountCreation:

    def login(self, Username=None, Password=None):
        Username = input("Enter your username: ")
        Password = input("Enter your Password: ")

        if not len(Username or Password) < 1:
            if True:
                db = open("credentials.txt", "r")
                d = []
                f = []
                for i in db:
                    a, b = i.split(",")
                    b = b.strip()
                    c = a, b
                    d.append(a)
                    f.append(b)
                    data = dict(zip(d, f))
                try:
                    if Username in data:
                        hashed = data[Username].strip('b')
                        hashed = hashed.replace("'", "")
                        hashed = hashed.encode('utf-8')

                        try:
                            if bcrypt.checkpw(Password.encode(), hashed):

                                print("Login success!")
                                print("Hi", Username)
                            else:
                                print("Wrong password")
                                self.login()
                        except:
                            print("Incorrect passwords or username")
                            self.login()
                    else:
                        print("Username doesn't exist")
                        self.login()
                except:
                    print("Password or username doesn't exist")
                    self.login()
            else:
                print("Error logging into the system")
                self.login()

        else:
            print("Please attempt login again")
            self.login()

    def signup(self, Username=None, Password1=None, Password2=None):
        Username = input("Enter a username:")
        Password1 = input("Create password:")
        Password2 = input("Confirm Password:")
        db = open("credentials.txt", "r")
        d = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            c = a, b
            d.append(a)
        if not len(Password1) <= 8:
            db = open("credentials.txt", "r")
            if not Username == None:
                if len(Username) < 1:
                    print("Please provide a username")
                    self.signup()
                elif Username in d:
                    print("Username exists")
                    self.signup()
                else:
                    if Password1 == Password2:
                        Password1 = Password1.encode('utf-8')
                        Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())

                        db = open("credentials.txt", "a")
                        db.write(Username+", "+str(Password1)+"\n")
                        print("User created successfully!")
                        print("Please login to proceed")
                        db.close()
                        self.login()
                    else:
                        print("Passwords do not match")
                        self.signup()
        else:
            print("Password too short")
            self.signup()
