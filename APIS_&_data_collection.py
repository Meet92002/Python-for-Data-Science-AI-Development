# Pandas is an API
# REST APIs
# Quiz

# Explanation of the NBA API + Pandas Code

# This code does 4 main things:

# 1. Creates a simple Pandas DataFrame
# 2. Gets NBA team information
# 3. Finds the Golden State Warriors team ID
# 4. Loads Warriors game data and compares home vs away performance

# Part 1: Creating a simple Pandas DataFrame


import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder


# These lines import libraries:

# * pandas → used for tables and data
# * matplotlib.pyplot → used to make graphs
# * teams → gets NBA team information
# * leaguegamefinder → gets game information from NBA API


dict = {'a':[11,21,31], 'b':[12,22,32]}
df = pd.DataFrame(dict)


# The dictionary looks like this:

{
    'a': [11,21,31],
    'b': [12,22,32]
}


# pd.DataFrame(dict) converts it into a table:

# |   | a  | b  |
# | - | -- | -- |
# | 0 | 11 | 12 |
# | 1 | 21 | 22 |
# | 2 | 31 | 32 |

type(df) # This checks the type of df.
# Output:
# pandas.core.frame.DataFrame

# That means df is a DataFrame.

df.head() #shows the first 5 rows.
# Since there are only 3 rows, it shows all of them.

df.mean()

# It finds the average of each column:

# * Column a: (11 + 21 + 31) / 3 = 21
# * Column b: (12 + 22 + 32) / 3 = 22

# Output:
# a    21.0
# b    22.0

# Part 2: The one_dict() Function

def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}

    for dict in list_dict:
        for key, value in dict.items():
            out_dict[key].append(value)

    return out_dict

# The NBA API returns data like this:

[
    {'id': 1610612737, 'nickname': 'Hawks'},
    {'id': 1610612738, 'nickname': 'Celtics'},
    {'id': 1610612744, 'nickname': 'Warriors'}
]

# That is a list of many dictionaries.

# The function converts it into:

{
    'id': [1610612737, 1610612738, 1610612744],
    'nickname': ['Hawks', 'Celtics', 'Warriors']
}

# This format is easier to turn into a DataFrame.

# Part 3: Getting NBA Team Data

nba_teams = teams.get_teams()

# This gets information about every NBA team.

# Example of first few teams:

nba_teams[0:3]

# Might return something like:

[
 {'id': 1610612737, 'nickname': 'Hawks'},
 {'id': 1610612738, 'nickname': 'Celtics'},
 {'id': 1610612739, 'nickname': 'Cavaliers'}
]

dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)

# This changes the list of dictionaries into a DataFrame.

# The DataFrame may look like:

# | id         | nickname |
# | ---------- | -------- |
# | 1610612737 | Hawks    |
# | 1610612738 | Celtics  |
# | 1610612744 | Warriors |

df_warriors = df_teams[df_teams['nickname'] == 'Warriors']

# This filters the table and keeps only the row where nickname is `Warriors`.

# Result:

# | id         | nickname |
# | ---------- | -------- |
# | 1610612744 | Warriors |

id_warriors = df_warriors[['id']].values[0][0] #This extracts only the ID number.

# Step by step:

df_warriors[['id']]

# returns:
#        id
# 0 1610612744

# Then:

# .values

# turns it into:

[[1610612744]]

# Then:

[0][0]

# gets the first row and first column:

1610612744

# So:

id_warriors = 1610612744

# Part 4: Downloading Warriors Game Data

# Instead of calling the NBA website directly, this code downloads a saved file.

import requests

# requests is used to download data from the internet.


filename = "https://.../Golden_State.pkl"


# This is the link to the file.

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

# This function:

# 1. Goes to the URL
# 2. Downloads the file
# 3. Saves it on your computer

download(filename, "Golden_State.pkl")# This downloads the file.

games = pd.read_pickle(file_name)


# A .pkl file stores a Python object.

# read_pickle() loads it into a DataFrame named games

# The table may contain columns like:

# | GAME_DATE  | MATCHUP     | PLUS_MINUS |
# | ---------- | ----------- | ---------- |
# | 2023-01-10 | GSW vs. TOR | 15         |
# | 2023-01-15 | GSW @ TOR   | -8         |


# Part 5: Home Games vs Away Games

games_home = games[games['MATCHUP'] == 'GSW vs. TOR']
games_away = games[games['MATCHUP'] == 'GSW @ TOR']

# These lines separate games:

# * GSW vs. TOR = Warriors played at home against Toronto
# * GSW @ TOR = Warriors played away at Toronto

# So:

# * games_home contains home games
# * games_away  contains away games

games_home['PLUS_MINUS'].mean()
games_away['PLUS_MINUS'].mean()

# means:

# * Positive number → Warriors won by that many points
# * Negative number → Warriors lost by that many points

# Example:

# | PLUS_MINUS |
# | ---------- |
# | 10         |
# | 15         |
# | -5         |

# Average:

(10 + 15 - 5) / 3 = 6.67


# If home average is bigger than away average, Warriors play better at home.

# Part 6: Plotting the Graph

fig, ax = plt.subplots() # This creates a blank graph.

games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)

# These two lines draw two lines on the same graph:

# * Away games line
# * Home games line

# x= 'GAME_DATE' → date on the bottom
# y='PLUS_MINUS' → score difference on the side

ax.legend(["away", "home"])

# This adds labels to the graph.
# The graph helps you compare whether Warriors perform better at home or away.
plt.show() #This displays the graph.




