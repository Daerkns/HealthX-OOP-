from login import AccountCreation
from activities import HealthyActivity


def main():

    account = AccountCreation()

    print("""
        ======  Welcome to HealthX  ======
        1. Create New Account
        2. Sign in to your Account
        """)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        account.signup()
    elif ch == 2:
        account.login()
    else:
        print("Wrong Choice!")
        exit()

    print("Welcome to HealthX!\nWhat do you want to do?\n1. Healthy Activity Reminder\n2. Exit Program")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        he = HealthyActivity()
        he.activity()
    elif choice == 2:
        exit()
    else:
        print("Error in input.")
        exit()


if __name__ == '__main__':
    main()
