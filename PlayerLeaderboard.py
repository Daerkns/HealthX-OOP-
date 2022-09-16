from operator import mod
import pandas as pd
import os.path


class LB:

    def leaderboard():
        print("     LEADERBOARD")
        if os.path.isfile('leaderboard.csv'):
            data = pd.read_csv('leaderboard.csv')
            data['HealthPoints'] = data['HealthPoints'].astype('int64')
            dfsorted = data.sort_values(
                by='HealthPoints', ascending=False)
            print(dfsorted)
        else:
            print("Leaderboard file does not exist. Players must use the application and gain points first to form leaderboard file.")
