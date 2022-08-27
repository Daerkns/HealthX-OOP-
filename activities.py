import winsound
import os
import random
import time


def confirmation():
    choice = int(input("Did you do the activity? 1/2 \n"))

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


def stretch():
    countdown(int(25))
    confirmation()


def water():
    countdown(int(15))
    confirmation()


def sunlight():
    countdown(int(10))
    confirmation()


def test():
    countdown(int(5))
    confirmation()


def play_sound():
    frequency = 500
    duration = 1000  # setting duration to 1000ms
    winsound.Beep(frequency, duration)


def countdown(t):

    while t:
        minute, second = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minute, second)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    play_sound()


def activity():
    opt = int(input("Which activity reminder do you want to set?\n1.Stretch break\n2.Drinking water\n3.Sunlight exposure\n4.Test/Experimental\n"))
    if opt == 1:
        stretch()
    elif opt == 2:
        water()
    elif opt == 3:
        sunlight()
    elif opt == 4:
        test()
    else:
        print("Invalid input")
