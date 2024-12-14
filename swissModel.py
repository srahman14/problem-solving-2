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

# pots = list(zip(pot_data["Pot1"], pot_data["Pot2"], pot_data["Pot3"], pot_data["Pot4"]))
# df = pd.DataFrame(pots, columns=pot_data.keys())

# Hold the team opponents
teamGames = {team: {"home": [], "away": []} for pot in pot_data.values() for team in pot}

# Shuffle the pots
for pot in pot_data.values():
    random.shuffle(pot)

# Each team has 4 home games and 4 away games -> 8 games in total
# No team can have more than 8 opponents
# Each team faces two opponents from each of the pots
# So lets start from the first pot till the last pot and add 1 home game and 1 away game for each

def pairTeams(teamGames, pot):
    # Initalize variables to track the pots

    for potNum in range(1, 5):
        currentPot = f"Pot{potNum}"
        teams = pot[currentPot]

        for team in teams:
            # Set the current home and away games for the current team
            homeGames = teamGames[team]["home"]
            awayGames = teamGames[team]["away"]

            # Track the remaining number of games to assign for home and away
            remainingHome = 4 - len(homeGames)
            remainingAway = 4 - len(awayGames)

            # If there are still remaining home games continue to assign:
            while remainingHome > 0:
                # Find an opponent from other pots
                for opponentPotNum in range(1, 5):
                    if remainingHome == 0:
                        break

                    if opponentPotNum == potNum:
                        continue

                    oppoentPot = f"Pot{opponentPotNum}"
                    opponents = pot[oppoentPot]

                    for opponent in opponents:
                        # Check if the number of home games is less than 4, for the current team
                        # and if the away games are less than 4 for opponent team
                        # Check if that team is not already playing the opponent team
                        if opponent not in homeGames and len(teamGames[opponent]["home"]) < 4:
                            homeGames.append(opponent)
                            teamGames[opponent]["away"].append(team)
                            remainingHome -= 1
                            break
                                    
                        # Check if the number of away games is less than 4, for the current team
                        # and if the home games are less than 4 for opponent team
                while remainingAway > 0:
                    for potNumOpponent in range(1, 5):
                        if remainingAway == 0:
                            break
                        if opponentPotNum == potNum:
                            continue
                    oppoentPot = f"Pot{opponentPotNum}"
                    opponents = pot[oppoentPot]

                    for opponent in opponents:
                        # Check if the number of home games is less than 4, for the current team
                        # and if the away games are less than 4 for opponent team
                        # Check if that team is not already playing the opponent team
                        if opponent not in awayGames and len(teamGames[opponent]["away"]) < 4:
                            awayGames.append(opponent)
                            teamGames[opponent]["home"].append(team)
                            remainingAway -= 1
                            break             
    return teamGames

result = pairTeams(teamGames, pot_data)
print(result)

def validateTeamGames(teamGames):
    for team, matches in teamGames.items():
        home_games = len(matches["home"])
        away_games = len(matches["away"])
        total_games = home_games + away_games

        if home_games != 4:
            print(f"Error: {team} has {home_games} home games!")
        if away_games != 4:
            print(f"Error: {team} has {away_games} away games!")
        if total_games != 8:
            print(f"Error: {team} has {total_games} total games!")
            
    print("Validation complete.")

# Call the function with your teamGames dictionary
validateTeamGames(result)
