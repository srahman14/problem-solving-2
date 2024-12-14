import random
import copy
import time

# Each list has 8 items 
matrix = [
 [15, 16, 17, 18, 19, 20, 21, 22],
 [14, 39, 40, 41, 42, 43, 44, 23],
 [13, 38, 55, 56, 57, 58, 45, 24],
 [12, 37, 54, 63, 64, 59, 46, 25],
 [11, 36, 53, 62, 61, 60, 47, 26],
 [10, 35, 52, 51, 50, 49, 48, 27],
 [9, 34, 33, 32, 31, 30, 29, 28],
 [8, 7, 6, 5, 4, 3, 2, 1]
]
# Get the size of the grid
size = len(matrix)

# This code was provided in the problem-context - it was not implicity stated if I could
# not use this code or not, but I would have used a similar function
def showBoard(size):
    for row in range(size):
     for col in range(size):
        # Access the number to be displayed (from 1 to 64)
        number = matrix[row][col]
        # Print the number, centred and with a width of 6 for proper alignment
        print(f"| {number:^6} ", end="")
     print("|") # Print the right border of the row
     print()

# This is to add the symbols for the bridges and hotels to the matrix i.e. (Bi, Hi, where i is a number)
def initialisePrevPositions():
    # Count here is to 
    count = 1
    for i in bridges:
        # Mapping function here used to map on the symbols at specific tiles 
        mapping(i, f"B{count}")
        # Here bridgesPrev is a dictionary to hold the symbols and its specific tile
        # i.e. 'B1': 10, so I can reset the positions of those tiles after the players pass it
        bridgesPrev[f"B{count}"] = i
        count += 1
    
    # I use the same logic as above for hotels
    count = 1
    for i in hotels:
        mapping(i, f"H{count}")
        hotelsPrev[f"H{count}"] = i
        count += 1
# The bridges that map to their tiles they jump to, i.e. tile 4 bridges you to tile 9
bridges = {
   4: 9, 8: 15, 12: 20, 18: 30,
   24: 34, 29: 34, 35: 39, 40: 50,
   46: 52, 50: 53, 51: 57,
}

# This will hold the symbols (B1, B2, ..., Bn)and their corresponding tiles
bridgesPrev = {}

# The hotels that map to if a turn should be skipped or not, each tile holds two values isHotel 
# which will help logic to skip a turn for a player, as well as occupied, if the hotel is empty or not
hotels = {
   10: {"isHotel": True, "occupied": False}, 21: {"isHotel": True, "occupied": False}, 32: {"isHotel": True, "occupied": False},
   38: {"isHotel": True, "occupied": False}, 45: {"isHotel": True, "occupied": False}, 57: {"isHotel": True, "occupied": False},
   61: {"isHotel": True, "occupied": False},
}

# This will hold the symbols (H1, H2, ..., Hn) and their corresponding tiles
hotelsPrev = {}

# This function is to return the symbol of a bridge according to its position on the 
# board, i.e. position 4 => returns B1, this is useful for resetting positions
def getBridgePrev(pos):
    # Getting the index of the position of the current position of the player
    # from a list of the values of all positions of the bridges
    indexOfBridge = list(bridgesPrev.values()).index(pos)
    # Getting the corresponding key i.e. symbol B1, using the index, as the index
    # of both keys and values will match in the lists
    keyBridge, valueBridge = list(bridgesPrev.items())[indexOfBridge]
    # Returning the symbol for the bridge
    return keyBridge

# This function is to return the symbol of a hotel according to its position on the 
# board, i.e. position 10 => returns H1, this is useful for resetting positions
def getHotelPrev(pos):
    # Getting the index of the position of the current position of the player
    # from a list of the values of all positions of the hotels
    indexOfHotel= list(hotelsPrev.values()).index(pos)
    # Getting the corresponding key i.e. symbol H1, using the index, as the index
    # of both keys and values will match in the lists
    keyHotel, valueHotel = list(hotelsPrev.items())[indexOfHotel]
    # Returning the symbol for the hotel
    return keyHotel

# Mapping function, to actually show the players, bridges, and hotels symbols on the 
# grid/board - given two parameters, position and player, i.e. a position is given, such as 4
# and a player/symbol, such as P1, P2, H1 etc
def mapping(pos, player):
    # These variables are used to track if the 'player'/symbol given is a bridge/hotel
    bridgePrev = None
    hotelPrev = None

    # Specifically here, if a bridge is found then bridgePrev will be equal to the symbol of the
    # given tile
    try:
        bridgePrev = getBridgePrev(pos)
        # print("BRIDGE PREV: ", bridgePrev) # Use for debugging
    except ValueError:
        # if no bridge found, then do nothing, this is preventive, to avoid the program crashing
        pass

    # Specifically here, if a hotel is found then hotelPrev will be equal to the symbol of the
    # given tile
    try:
        hotelPrev = getHotelPrev(pos)
        # print("HOTEL PREV: ", hotelPrev) # Use for debugging
    except ValueError:
        # if no hotel found, then do nothing, this is preventive, to avoid the program crashing
        pass

    # The decided tile to map is decided using this conditional statement, only one can be True
    # whatever is true will be chosen to map to
    tileToMap = bridgePrev or hotelPrev or pos
    # Iterate through each row and cell, to find the exact cell equal to the player/symbol, then
    # set that cell/tile to the player/symbol
    for row in matrix:
        for cell in row:
            if cell == tileToMap:
                row[row.index(cell)] = player
                return


# To set all of the special tiles before beginning game
initialisePrevPositions()

# The function - which took the longest to configure - to reset the positions after the players have
# moved positions, i.e. after a new turn to change it back to what it previously was, hence the names
# of the dictionaries, bridgesPrev, hotelsPrev. 
# Once again, this takes two arguments (position and player/symbol) and essentially does the opposite of 
# the mapping function.
def resetPosition(pos, player):
    # Iterate through each row
    for row in matrix
        # i, here being index of current element, cell, here the actual element - this is due to using the
        # enumerate function
        for i, cell in enumerate(row):
            # if the cell/tile is equal to the player e.g. 'P1'
            if cell == player:
                # if the position of that player, e.g. 10, is in the dictionaries that match tiles to symbols
                if pos in bridgesPrev.values():
                    # Then we get back the symbol from that dictinoary using the function defined before
                    symbol = getBridgePrev(pos)
                    # and set it to the position of the old position of the player
                    row[i] = symbol
                # Same logic is applied for hotel symbols on the board
                elif pos in hotelsPrev.values():
                    symbol = getHotelPrev(pos)
                    row[i] = symbol
                # if the tile is equal to neither of the symbols, then naturally return the number of the tile
                # and set it to the old position of the player
                else:
                    row[i] = pos
                return
# Function to check if a tile is special -> if so, then do the specific action related to that special tile
def checkSpecialTiles(playerPos, player):
    # If the position of the player is in the positions of the hotel tiles, then we apply the skip 
    if playerPos in hotels:
        # If the tile is not already occupied
        if not hotels[playerPos]["occupied"]:
            print(f"{player} landed on a hotel at position {playerPos}! {player} skipping their next turn :c")
            # Then set occupied to true, and return the player position
            hotels[playerPos]["occupied"] = True
            return playerPos
    # If the position of the player is in the positions of the bridges tiles, then we apply the bridge 
    if playerPos in bridges:
        print(f"{player} landed on a bridge! Moving to {bridges[playerPos]} from {playerPos}")
        # the new position is accessed from the dictionary of bridges i.e. bridges[4] => 9
        newPos = bridges[playerPos]
        # Then we map the new position with the player given
        mapping(newPos, player)
        # return the new position to update the player's score
        return newPos
    # if the tile is not special, then just return the player position as nothing changed
    # the player position is returned in the hotel tile check too, as the main thing is to change
    # the occupied state to true, so that the player's next turn skips
    return playerPos

# Function to check if the player has a won
def checkWinCondition(playerPos, player):
    # Winning tile
    winner = 64
    # If the player position tile is equal to 64, then that player has won
    if playerPos == winner:
        print(f"{player} wins the game by landing on 64!")
        return True
    # If the player has gone over 64, then it must bounce back
    elif playerPos > winner:
        # Find the amount of tiles to bounce back
        bounceBack = playerPos - winner
        # Assign the player position to the bounced back position
        playerPos = winner - bounceBack
        print(f"{player} rolled too high by {bounceBack}! Bouncing back to tile {playerPos}")
    return playerPos

# Flag for win
win = False
# To tracked skipped turns -> hotels
skippedTurnOne = False
skippedTurnTwo = False

# Starting positions of players => 1
playerOnePos = 1
playerTwoPos = 1
# Old positions of players -> used for restting positions after new turns
previousPositionOne = 0
previousPositionTwo = 0

while not win:
    time.sleep(1)
    # reset position at the start of every iteration, important so board will have 
    # at least two players at once i.e. P1, P2, or P1/2
    # reset position one and two
    if previousPositionOne != 0:
       resetPosition(previousPositionOne, "P1")
    if previousPositionTwo != 0:
        resetPosition(previousPositionTwo, "P2")
    # when positions are equal then have to change player parameter to P1/2, to correctly reset 
    if previousPositionOne == previousPositionTwo:
        resetPosition(previousPositionOne, "P1/2")
    
    # If player 1 turn is not skipped
    if not skippedTurnOne:
        diceRollOne = random.randint(1, 6)
        print("Player 1 Turn: \n")
        input("Enter to roll the dice! ")
        print("Dice roll: ", end =" ")
        time.sleep(1.2)
        print(diceRollOne)
        # Update score of the player 1
        playerOnePos += diceRollOne
        print(f"Player one score: {playerOnePos}")
        # Check if the player has won, avoids going over to player 2's turn when not needed
        playerOnePos = checkWinCondition(playerOnePos, "P1")
        if playerOnePos is True:
            win = True
            break
        # Check if player has landed on a special tile
        playerOnePos = checkSpecialTiles(playerOnePos, "P1")
        # Check if the player has landed on a hotel and if the hotel is occupied
        # If occupied => skip the player's turn (set skippedTurnOne to True)
        skippedTurnOne = hotels.get(playerOnePos, {}).get("occupied", False)
    else:
        # A turn is skipped
        print("Player 1 turn skipped :c")
        # Reset the skippedTurn back to False so after skipped turn it goes back to a normal turn
        skippedTurnOne = False

    # All the same logic used from above for player 2 also
    if not skippedTurnTwo:
        diceRollTwo = random.randint(1, 6)
        print("Player 2 Turn: \n")
        # input("Enter to roll the dice! ")
        print("Dice roll: ", end =" ")
        time.sleep(1.2)
        print(diceRollTwo)
        playerTwoPos += diceRollTwo
        print(f"Player two score: {playerTwoPos}")
        playerTwoPos = checkWinCondition(playerTwoPos, "P2")
        if playerTwoPos is True:
            win = True
            break
        playerTwoPos = checkSpecialTiles(playerTwoPos, "P2")
        skippedTurnTwo = hotels.get(playerTwoPos, {}).get("occupied", False)
    else:
        print("Player 2 turn skipped :c")
        skippedTurnTwo = False

    # If the scores of the players are equal, then set that tile to a shared symbol 
    # for the players e.g. P1/2
    if playerOnePos == playerTwoPos:
       mapping(playerOnePos, f"P1/2")
    else:
        # otherwise, map it individually as normal
        mapping(playerOnePos, "P1") 
        mapping(playerTwoPos, "P2")

    # print(f"Player 1 position after mapping: {playerOnePos}") # Debugging statements
    # print(f"Player 2 position after mapping: {playerTwoPos}") # Debugging statements

    previousPositionOne = playerOnePos
    previousPositionTwo = playerTwoPos

    # print("Previous position one: ", previousPositionOne) # Debugging statements
    # print("Previous position two: ", previousPositionTwo) # Debugging statements

    time.sleep(2)
    print("\nGame of Goose: \n")
    # Show the board after every turns
    showBoard(size)