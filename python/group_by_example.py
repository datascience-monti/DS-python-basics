# -*- coding: utf-8 -*-
"""
Kaggle DataSet Link: https://www.kaggle.com/drgilermo/nba-players-stats
Files: (1) player_data.csv  (2) Players.csv  (3)  Seasons_Stats.csv
"""
import os
os.chdir('C:/Users/Administrator/Documents/AnalysisProjects/TeachingDS/Basketball/')

import pandas as pd


""" Read In My NBA DATA """
player_data = pd.read_csv('Data/KaggleNBA/player_data.csv', index_col = 0)        #Player College Data
players = pd.read_csv('Data/KaggleNBA/Players.csv', index_col = 0)                #Player Basic Info Data
season_stats = pd.read_csv('Data/KaggleNBA/Seasons_Stats.csv', index_col = 0)     #Each Row = One Season Of Stats For One Player



""" Season Stats Info """
print(season_stats.columns.tolist()) #Gives Me The Columns In Compressed Format, Easier To See All Then using .info()

"""
Some Common Basketball Data Columns
Year, Player, Age, Tm (Team), PTS
"""


""" GROUP BY Scenario """
""" What We Know About The DataSet 
        Year    - We Have A Dataset That Spans Years 1950 - 2017   |   print('Min Year:',season_stats.Year.min(), ', Max Year:',season_stats.Year.max())
        Player  - We Have 3922 Unique Players In This Data Set     |   print(len(season_stats.Player.unique()))  
        Age     - Age Ranges From 18 - 44                          |   print('Min Age:',season_stats.Age.min(), ', Max Age:',season_stats.Age.max())
        TM      - 70 Unique Tm Identifiers                         |   print('Number Of Unique Seasons:',len(season_stats.Tm.unique())) 
        PTS     - Season Pts Range From 0 - 4029                   |   print('Min PTS:',season_stats.PTS.min(), ', Max PTS:',season_stats.PTS.max())
        
Some Simple Questions Where We Would Use Group By

(1) Which Player(s) Has Averaged The Most Season Pts Over Their Career?
(2) 
(3) 
        
""" 

""" Code To Solve Question (1) """
player_season_pts_avg = season_stats.groupby(['Player'])['PTS'].mean().reset_index()
player_season_pts_avg.sort_values(by='PTS', ascending = False, inplace = True)
player_season_pts_avg.reset_index(drop = True, inplace = True)
player_season_pts_avg.head(5)




""" Code To Solve Question (2) """





""" Code To Solve Question (3) """



