# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd
PATH = "/Users/katharina/ds/metis/metisgh/prework/dsp/"

fb = pd.read_csv(PATH + "python/football.csv")
fb["goalDiff"] = fb['Goals Allowed'] - fb["Goals"]
print(fb.loc[fb["goalDiff"] == min(abs(fb["goalDiff"])), "Team"].to_string(index = False)) 
# Aston_Villa

