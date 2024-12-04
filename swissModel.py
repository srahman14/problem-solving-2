# Input/Output:

# The program starts by showing the four pots of teams.
# After the draw for each team, display their opponents.
# Allow the user to query the draws by team name after the full league draw is complete.    

# Create the four pots and place into a list

import pandas as pd
import random

pot_data = {
    "Pot1": [
        "Manchester United", "Real Madrid", "Bayern Munich", "Barcelona", 
        "Lazio", "Deportivo La Coruña", "Arsenal", "Juventus", 
        "Paris Saint-Germain"
    ],
    "Pot2": [
        "Valencia", "AC Milan", "Inter Milan", "Porto", "Chelsea", 
        "Dynamo Kyiv", "Galatasaray", "AS Monaco", "Bayer Leverkusen"
    ],
    "Pot3": [
        "Leeds United", "Lyon", "PSV Eindhoven", "Aston Villa", 
        "Rangers", "Feyenoord", "Anderlecht", "Olympiacos", 
        "Panathinaikos"
    ],
    "Pot4": [
        "Celtic", "Club Brugge", "Stuttgart", "Herfølge BK", 
        "Helsingborgs IF", "Rosenborg", "Sturm Graz", 
        "Sparta Prague", "1860 Munich"
    ]
}

data = list(zip(pot_data["Pot1"], pot_data["Pot2"], pot_data["Pot3"], pot_data["Pot4"]))
df = pd.DataFrame(data, columns=pot_data.keys())

# Hold the team opponents

teamGames = {team: {"home": [], "away": []} for pot in pot_data.values() for team in pot}

# Randomly select two teams:
def pairTeams(pot1, pot2):
    matches = []
    random.shuffle(pot1)
    random.shuffle(pot2)

    for team1, team2 in zip(pot1, pot2):
        if random.choice([True, False]):
            home, away = team1, team2
        else:
            away, home = team2, team1
        
        matches.append((home, away))
        teamGames[home]["home"].append(away)
        teamGames[away]["away"].append(home)
    
    return matches


matches = []

# Pot1 vs Pot2
matches.extend(pairTeams(pot_data["Pot1"], pot_data["Pot2"]))

# Pot1 vs Pot3
matches.extend(pairTeams(pot_data["Pot1"], pot_data["Pot3"]))

# Pot1 vs Pot4
matches.extend(pairTeams(pot_data["Pot1"], pot_data["Pot4"]))

# Pot2 vs Pot3
matches.extend(pairTeams(pot_data["Pot2"], pot_data["Pot3"]))

# Pot2 vs Pot4
matches.extend(pairTeams(pot_data["Pot2"], pot_data["Pot4"]))

# Pot3 vs Pot4
matches.extend(pairTeams(pot_data["Pot3"], pot_data["Pot4"]))

# Display the results
count = 0
for match in matches:
    home, away = match
    print(f"Home: {home} vs Away: {away}")
    count+=1

print(count)