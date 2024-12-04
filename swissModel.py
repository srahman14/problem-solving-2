# Input/Output:

# The program starts by showing the four pots of teams.
# After the draw for each team, display their opponents.
# Allow the user to query the draws by team name after the full league draw is complete.    

# Create the four pots and place into a list

import pandas
import random

Pot1 = [
    "Manchester United",
    "Real Madrid",
    "Bayern Munich",
    "Barcelona",
    "Lazio",
    "Deportivo La Coruña",
    "Arsenal",
    "Juventus",
    "Paris Saint-Germain"
]


Pot2 = [
    "Valencia",
    "AC Milan",
    "Inter Milan",
    "Porto",
    "Chelsea",
    "Dynamo Kyiv",
    "Galatasaray",
    "AS Monaco",
    "Bayer Leverkusen"
]


Pot3 = [
    "Leeds United",
    "Lyon",
    "PSV Eindhoven",
    "Aston Villa",
    "Rangers",
    "Feyenoord",
    "Anderlecht", 
    "Olympiacos", 
    "Panathinaikos"
]

Pot4 =  [
    "Celtic",
    "Club Brugge",
    "Stuttgart", 
    "Herfølge BK",
    "Helsingborgs IF",
    "Rosenborg",
    "Sturm Graz",
    "Sparta Prague",
    "1860 Munich"
]

# Use of zip combines all the pots into tuples 
# This also formats it in a readable way for panda
# So that the teams are stacked, as the tuples are the rows
# data = list(zip(Pot1, Pot2, Pot3, Pot4))
# headers = ["Pot1", "Pot2", "Pot3", "Pot4"]
# # Creating dataframe with columns holding header names
# df = pandas.DataFrame(data, columns=headers)

length = len(Pot1)

print(random.randrange(1, length))