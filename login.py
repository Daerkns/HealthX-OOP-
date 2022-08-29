import imp
import hashlib
import sys


class AccountCreation:

    def signup(self):
        email = input("Enter email address: ")
        pwd = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        type = int(input("User type? 1. for Player 2. for Administrator"))
        while True:
            if type == 1 or 2:
                if conf_pwd == pwd:
                    enc = conf_pwd.encode()
                    hash1 = hashlib.md5(enc).hexdigest()
                    with open("credentials.txt", "w") as f:
                        f.write(email + "\n")
                        f.write(hash1 + "\n")
                        if type == 1:
                            f.write("Player")
                        elif type == 2:
                            f.write("Administrator")
                    f.close()
                    print("You have registered successfully!")
                    break
                else:
                    print("Password is not same as above! \n")
            else:
                sys.exit("Error in input. Please enter 1 or 2.")

            if conf_pwd == pwd:
                enc = conf_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                with open("credentials.txt", "w") as f:
                    f.write(email + "\n")
                    f.write(hash1 + "\n")
                    if type == 1:
                        f.write("Player")
                    elif type == 2:
                        f.write("Administrator")
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
            stored_email, stored_pwd, type = f.read().split("\n")
        f.close()

        if email == stored_email and auth_hash == stored_pwd and type == "Player":
            print("Player login was successful!")
        elif email == stored_email and auth_hash == stored_pwd and type == "Administrator":
            print("Administrator login was successful!")
        else:
            print("Login failed! Wrong Credentials or Credentials do not exist. \n")
