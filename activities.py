from operator import index
import winsound
import os
import random
import time
import pandas as pd
import os.path


class HealthyActivity:

    def confirmation(self, activity_name):
        choice = int(input(
            "Did you do the activity?\nIf yes --> enter 1\nIf no  --> enter 2\n1. Yes\n2. No\n"))

        praise = ["There you go! You've done the right thing.\n",
                  "Keep up the good work.\n",
                  "See? It wasn't that hard.\n",
                  "You've made yourself healthier. Feel good about it!\n",
                  "Small things add up. Good job!\n",
                  "Well done!\n",
                  "That's a healthy decision!\n",
                  "Excellent!\n",
                  "You'll thank yourself for this in the future.\n",
                  "Wonderful!\n"]
        random_praise = random.choice(praise)

        next_time = ["Better luck next time!\n",
                     "Awww, too bad.\n",
                     "Hopefully, you'll do it next time!\n",
                     "There's always another time.:3 \n",
                     "No problem, you can do it later.\n",
                     "It's okay to skip once in a while.\n",
                     "Don't worry, give it a shot next time.\n",
                     "Try again later.\n"]
        random_next_time = random.choice(next_time)
        if choice == 1:
            print(random_praise)
            if activity_name == 'stretch':
                self.addpoints(int(100))
            elif activity_name == 'water':
                self.addpoints(int(300))
            elif activity_name == 'sunlight':
                self.addpoints(int(1000))
            elif activity_name == 'test':
                self.addpoints(int(200))
        elif choice == 2:
            print(random_next_time)
        else:
            print("Invalid input")

    def stretch(self):
        activity_name = 'stretch'
        self.countdown(int(25))
        self.confirmation(activity_name)

    def water(self):
        activity_name = 'water'
        self.countdown(int(15))
        self.confirmation(activity_name)

    def sunlight(self):
        activity_name = 'sunlight'
        self.countdown(int(10))
        self.confirmation(activity_name)

    def test(self):
        activity_name = 'test'
        self.countdown(int(5))
        self.confirmation(activity_name)

    def play_sound(self):
        frequency = 500
        duration = 1000  # setting duration to 1000ms
        winsound.Beep(frequency, duration)

    def addpoints(self, points):

        with open('currentuser.txt') as file:
            current_user = file.read()  # detecting the current logged in user
            print("You are currently logged in as: " + current_user)

        if os.path.isfile('leaderboard.csv'):
            data = pd.read_csv('leaderboard.csv')
            placeholder = data['Player'].str.contains(current_user).sum()
            if placeholder > 0:
                data.loc[data['Player'] == current_user,
                         'HealthPoints'] += points
                data.to_csv('leaderboard.csv', mode='w+', index=False)

                print(f"{current_user}'s stats were updated on leaderboard file.")

            elif placeholder == 0:
                data.loc[len(data.index)] = [current_user, points]
                data.to_csv('leaderboard.csv', mode='w+', index=False)

                print(
                    f"New entry of {current_user}'s stats was added to Leaderboard.")

        else:
            leaderboard = [[current_user, points]]
            df = pd.DataFrame(leaderboard, columns=['Player', 'HealthPoints'])
            df.to_csv('leaderboard.csv', index=False)
            print(
                f"Leaderboard file was created along with {current_user}'s stats.")

        #leaderboard = dict()
        # with open("leaderboard.txt", 'r+') as file2:
        # for name, p in zip(file2, file2):
        #leaderboard[name.strip()] = {"HPoints": int(p)}
        # if leaderboard['name'] == current_user:
        #leaderboard['HPoints'] += points
        # else:
        # pass

        #print("New values: ")
        # print(leaderboard)

        # with open('leaderboard.txt', 'a') as file2:
        #file2.write(current_user + " " + str(points))

        # leaderboard = {'Username': current_user, 'Points': points}

        # with open('leaderboard.txt') as file2: # reading all the lines in leaderboard file. Format of leaderboard file = each line has username and current points
        #    leaderboard = file2.readlines()
        #    if current_user in leaderboard:

    def countdown(self, t):

        while t:
            minute, second = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(minute, second)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        self.play_sound()

    def activity(self):
        opt = int(input("Which activity reminder do you want to set?\n1. Stretch break\n2. Drinking water\n3. Sunlight exposure\n4. Test/Experimental\n5. Go Back\n6. Exit Program\n"))
        if opt == 1:
            self.stretch()
        elif opt == 2:
            self.water()
        elif opt == 3:
            self.sunlight()
        elif opt == 4:
            self.test()
        elif opt == 5:
            pass
        elif opt == 6:
            exit()
        else:
            print("Invalid input")
