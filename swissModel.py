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

pots = list(zip(pot_data["Pot1"], pot_data["Pot2"], pot_data["Pot3"], pot_data["Pot4"]))
df = pd.DataFrame(pots, columns=pot_data.keys())

# Shuffle the pots
for pot in pot_data.values():
    random.shuffle(pot)

teams = [team for pot in pot_data.values() for team in pot]

def pairTeams(teams, pots):
    # Each team has 4 home games and 4 away games -> 8 games in total
    # No team can have more than 8 opponents
    # Each team faces two opponents from each of the pots

    # Args:
    # - teams (list): List of all teams
    # - pots (dict): keys => pot names and values => team names 

    # Return:
    # - dictionary: with all team games

    # Create team games for all teams
    teamGames = {team: [] for team in teams}

    for potName in pots:
        for team in teams:
            # Check for number of games for the current team
            totalGames = len(teamGames[team]) 

            # If a team already has 8 teams, then the iteration should skip
            if totalGames >= 8:
                continue

            # Generate opponents not already played against for current team to select
            # the team games for the current team
            opponentsToPlay = [
                # Get every team in the pot besides the team itself
                opponent for opponent in pots[potName]
                if opponent != team and 
                # The opponent should not already be playing the current team
                opponent not in teamGames[team]
                # The number of games for a opponent should not already be 8
                and len(teamGames[opponent]) < 8
            ]
            # If the number of games for any team is less than 8
            if len(teamGames[team]) < 8:
                # If the number of available teams is at least two, then we can assign
                # two teams to the current pot 
                if len(opponentsToPlay) >= 2:
                    opponents = random.sample(opponentsToPlay, 2)
                    teamGames[team].extend(opponents)

    
    return teamGames

# Requirement 1 - display the four pots:
print(df)
print()
# Requirement 2 - draw teams 
result = pairTeams(teams, pot_data)
# Requirement 3/4 - show draw of opponents 
def showOpponents(draws):
    for team, opponents in draws.items():
        print(f"\nDraw for {team}: ")
        # Variable to alternate between home and away
        currGame = "Home"
        
        for i in opponents:
            print(f"- {i} ({currGame})")
            # If this team was assigned home
            if currGame == "Home":
                # Then next team should be assumed away
                currGame = "Away"
            else:
                # Else it should be assigned to home
                currGame = "Home"
        input("\nEnter to view the next team")

showOpponents(result)

# Requirement 6 - specific team draws
def displaySpecificTeam(teams):
    # Variable to hold if the user would like to check for the draw of a specific team
    userInput = ""
    # If user input invalid input, then continue to ask until Y or N entered
    while userInput.lower().strip() != "y" or "n":
        userInput = str(input("Would you like to check for the draw of a specific team: (Y/N)"))

        if userInput.lower().strip() == "y" or "n":
            break
    # if a user enters N, then program should quit
    if userInput.strip().lower() == "n":
        print("Program exited")
        return False
    # Similar logic for displayOpponents() func, used to alternate between home and away
    currGame = "Home"
    while userInput.lower().strip() == "y":
        teamChoice = ""
        # if team not in the teams list, then repeat asking for the team name
        # use the .title() to capitalize each of the first letters in the team name
        while teamChoice.title() not in teams:
            teamChoice = str(input("Enter the name of the team you would like to view: "))
            if teamChoice.title() in teams:
                break
        # Variable to hold the team opponent names in a list 
        teamSelected = teams[teamChoice.title()]
        print(f"Draw for {teamChoice}: ")
        # Where i, is the opponent
        for i in teamSelected:
            print(f"- {i} ({currGame})")
            if currGame == "Home":
                currGame = "Away"
            else:
                currGame = "Home"
        break
    
while True:
    if not displaySpecificTeam(result):
        break
    else:
        displaySpecificTeam(result)
    