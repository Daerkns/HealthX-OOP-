from login import login, loginsystem


def main():

    account = login()

    while True:
        print("""
        ======  Welcome to HealthX  ======
        1. Create New Account
        2. Sign in to your Account
        """)

        choice = input("Enter Choice 1/2 : ")

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter an int")
            continue

        if choice == 1:
            account.signup()

        elif choice == 2:
            account.login()

        else:
            print("Invalid Input. Please enter 1 or 2.")
