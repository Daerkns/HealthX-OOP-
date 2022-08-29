import winsound
import os
import random
import time


class HealthyActivity:

    def confirmation(self):
        choice = int(input("Did you do the activity?\n1.Yes\n2. No \n"))

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
        elif choice == 2:
            print(random_next_time)
        else:
            print("Invalid input")

    def stretch(self):
        self.countdown(int(25))
        self.confirmation()

    def water(self):
        self.countdown(int(15))
        self.confirmation()

    def sunlight(self):
        self.countdown(int(10))
        self.confirmation()

    def test(self):
        self.countdown(int(5))
        self.confirmation()

    def play_sound(self):
        frequency = 500
        duration = 1000  # setting duration to 1000ms
        winsound.Beep(frequency, duration)

    def countdown(self, t):

        while t:
            minute, second = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(minute, second)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        self.play_sound()

    def activity(self):
        opt = int(input(
            "Which activity reminder do you want to set?\n1.Stretch break\n2.Drinking water\n3.Sunlight exposure\n4.Test/Experimental\n"))
        if opt == 1:
            self.stretch()
        elif opt == 2:
            self.water()
        elif opt == 3:
            self.sunlight()
        elif opt == 4:
            self.test()
        else:
            print("Invalid input")
