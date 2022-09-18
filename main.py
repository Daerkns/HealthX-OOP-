from login import AccountCreation
from activities import HealthyActivity
from PlayerLeaderboard import LB


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

    print("Welcome to HealthX!\nWhat do you want to do?")
    healthx()
    # with open('currentuser.txt', 'r') as file:
    #current_user = file.read()
    # print(current_user)


def healthx():
    choice = int(input(
        "Enter your choice: \n1. Healthy Activity Reminder\n2. View Leaderboard of Players\n3. Exit Program\n"))
    if choice == 1:
        he = HealthyActivity()
        he.activity()
    elif choice == 2:
        LB.leaderboard()
    elif choice == 3:
        exit()
    else:
        print("Error in input.")
    healthx()


if __name__ == '__main__':
    main()
