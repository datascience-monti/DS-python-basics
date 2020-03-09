# -*- coding: utf-8 -*-
"""
Kaggle DataSet Link: https://www.kaggle.com/drgilermo/nba-players-stats
Files: (1) player_data.csv  (2) Players.csv  (3)  Seasons_Stats.csv
"""
import os
os.chdir('C:/Users/{YourDirectoryHere}/') #Make Sure You Update Your Directory

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
(2) Which Age Has The Highest Max Pts In A Season And What Year Did This Occur ?
        
""" 

""" Code To Solve Question (1) """
player_season_pts_avg = season_stats.groupby(['Player'])['PTS'].mean().reset_index()
player_season_pts_avg.sort_values(by='PTS', ascending = False, inplace = True)
player_season_pts_avg.reset_index(drop = True, inplace = True)
player_season_pts_avg.head(5)


"""
              Player          PTS
0    Michael Jordan*  2152.800000
1  Wilt Chamberlain*  2122.062500
2     George Gervin*  2070.800000
3       LeBron James  2056.214286
4       Karl Malone*  1943.578947
"""



""" Code To Solve Question (2) """
age_season_pts_best = season_stats.groupby(['Age', 'Year'])['PTS'].max().reset_index()
age_season_pts_best.sort_values(by='PTS', ascending = False, inplace = True)
age_season_pts_best.reset_index(drop = True, inplace = True)
age_season_pts_best.head(5)

"""
    Age    Year     PTS
0  25.0  1962.0  4029.0
1  26.0  1963.0  3586.0
2  23.0  1987.0  3041.0
3  24.0  1961.0  3033.0
4  27.0  1964.0  2948.0
"""



















