from login import AccountCreation


def main():

    account = AccountCreation()

    while True:
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


if __name__ == '__main__':
    main()
