import hashlib


class Login:

    def signup(self):
        email = input("Enter email address: ")
        pwd = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        type = int(input("User type? 1. for Player 2. for Administrator"))
        while type == 1 or 2:
            continue
        else:
            print("Error")
        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open("credentials.txt", "w") as f:
                f.write(email + "\n")
                f.write(hash1 + "\n")

            f.close()
            print("You have registered successfully!")
        else:
            print("Password is not same as above! \n")

    def login(self):
        email = input("Enter email: ")
        pwd = input("Enter password: ")
        auth = pwd.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        with open("credentials.txt", "r") as f:
            stored_email, stored_pwd = f.read().split("\n")
        f.close()
        if email == stored_email and auth_hash == stored_pwd:
            print("Logged in Successfully!")
        else:
            print("Login failed! \n")
