import pandas as pd
import datetime
import time
import pickle
import numpy as np
import random
class ModelHelper():
    def __init__(self):
        pass
    def get_matchup(self, yr1, yr2, avg_df_year, teamA, gb_year, avg_df_year2, teamB, gb_year2):
        home = avg_df_year.loc[avg_df_year['TeamName_Clean'] == teamA]
        home = home[['AdjEM', 'AdjO', 'AdjD', 'AdjT', 'Luck', 'SOS_AdjEM',
        'SOS_OppO', 'SOS_OppD', 'NCSOS_AdjEM', 'WFGA',
        'WFGA3', 'WFTA', 'WOR', 'WDR', 'WAst', 'WTO', 'WStl', 'WBlk',
        'WPF']]
        away = avg_df_year2.loc[avg_df_year2['TeamName_Clean'] == teamB]
        away = away[['AdjEM', 'AdjO', 'AdjD', 'AdjT', 'Luck', 'SOS_AdjEM',
        'SOS_OppO', 'SOS_OppD', 'NCSOS_AdjEM', 'WFGA',
        'WFGA3', 'WFTA', 'WOR', 'WDR', 'WAst', 'WTO', 'WStl', 'WBlk',
        'WPF']]
        home_points = pd.merge(home, away, how='outer')
        away_points = pd.merge(away, home, how='outer')
        home_points = np.array(home_points).reshape(-1, 38)
        away_points = np.array(away_points).reshape(-1, 38)
        home_score = int(gb_year.predict(home_points))
        away_score = int(gb_year2.predict(away_points))
        OT_count = 0
        while home_score == away_score:
            OT_count += 1
            print(f'END OF REGULATION | {teamA}: {round(home_score,0)} | {teamB}: {round(away_score,0)}')
            print('-----------------------------------------')
            print(f'SIMMING {OT_count}OT')
            print('-----------------------------------------')
            home_score = home_score + random.randint(5, 15)
            away_score = away_score + random.randint(5, 15)
        else:
            print('FINAL')
            print('-----------------------------------------')
            # return (f'{yr1} {teamA}: {round(home_score,0)} | {yr2} {teamB}: {round(away_score,0)}')
            return [{'team': teamA, 'points': home_score}, {'team': teamB, 'points': away_score}]
            