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

def showBoard(size):
    for row in range(size):
     for col in range(size):
        # Access the number to be displayed (from 1 to 64)
        number = matrix[row][col]
        # Print the number, centred and with a width of 6 for proper alignment
        print(f"| {number:^6} ", end="")
     print("|") # Print the right border of the row
     print()

def initialisePrevPositions():
    count = 1
    for i in bridges:
        mapping(i, f"B{count}")
        bridgesPrev[f"B{count}"] = i
        count += 1
    
    count = 1
    for i in hotels:
        mapping(i, f"H{count}")
        hotelsPrev[f"B{count}"] = i
        count += 1
    
bridges = {
   4: 9, 8: 15, 12: 20, 18: 30,
   24: 34, 29: 34, 35: 39, 40: 50,
   46: 52, 50: 53, 51: 57,
}

bridgesPrev = {}

hotels = {
   10: 1, 21: 1, 30: 1,
   38: 1, 45: 1, 57: 1,
   61: 1,
}

hotelsPrev = {}

def getBridgePrev(pos):
    indexOfBridge = list(bridgesPrev.values()).index(pos)

    keyBridge, valueBridge = list(bridgesPrev.items())[indexOfBridge]

    return keyBridge

def getHotelPrev(pos):
    indexOfHotel= list(hotelsPrev.values()).index(pos)
    keyHotel, valueHotel= list(hotelsPrev.items())[indexOfHotel]

    return keyHotel


def mapping(pos, player):
    bridgePrev = None
    hotelPrev = None

    try:
        bridgePrev = getBridgePrev(pos)
    except ValueError:
        pass

    try:
        hotelPrev = getHotelPrev(pos)
    except ValueError:
        pass

    tileToMap = bridgePrev or hotelPrev or pos

    for row in matrix:
        for k in row:
            if k == tileToMap:
                row[row.index(k)] = player
                return

def resetPosition(pos):
    for row in matrix:
        for i, cell in enumerate(row):
            if cell == pos:
                if pos in bridgesPrev.values():
                    symbol = getBridgePrev(pos)
                    row[i] = symbol
                elif pos in hotelsPrev.values():
                    symbol = getHotelPrev.values()
                    row[i] = symbol
                else:
                    row[i] = pos


# To set all of the special tiles before beginning game
initialisePrevPositions()

win = False
# For hotels
skippedTurnOne = False
skippedTurnTwo = False

playerOnePos = 1
playerTwoPos = 1
previousPositionOne = 0
previousPositionTwo = 0

while not win:
    time.sleep(1)
    if previousPositionOne != 0:
       resetPosition(playerOnePos)
       previousPositionOne = playerOnePos
    if previousPositionTwo != 0:
        resetPosition(playerTwoPos)
        previousPositionTwo = playerTwoPos
    
    if playerOnePos in hotels and not skippedTurnOne:
       print("Player 1 turn skipped!")
       skippedTurnOne = True
    else:
        diceRollOne = random.randint(1, 6)
        print("Player 1 Turn: \n")
        input("Enter to roll the dice! ")
        print("Dice roll: ", end =" ")
        time.sleep(3)
        print(diceRollOne)
        playerOnePos += diceRollOne
        previousPositionOne = playerOnePos
        print(f"Player one score: {playerOnePos}")
        skippedTurnOne = False

    if playerTwoPos in hotels and not skippedTurnTwo:
       print("Player 2 turn skipped!")
       skippedTurnTwo = True
    else:
        diceRollTwo = random.randint(1, 6)
        print("Player 2 Turn: \n")
        input("Enter to roll the dice! ")
        print("Dice roll: ", end =" ")
        time.sleep(3)
        print(diceRollTwo)
        playerTwoPos += diceRollTwo
        previousPositionTwo  = playerTwoPos
        print(f"Player tow score: {playerTwoPos}")
        skippedTurnTwo = False

    #     if (playerOnePos in hotels):
    #        skippedTurnOne = True
    #     if (playerTwoPos in hotels):
    #        skippedTurnTwo = True

    
    if playerOnePos == playerTwoPos:
       mapping(playerOnePos, "P1/2")
    else:
        mapping(playerOnePos, "P1") 

        mapping(playerTwoPos, "P2")


    time.sleep(2)
    print("Game of Goose: \n")
    time.sleep(2)
    showBoard(size)


# MAPPING FUNCTION NOT WORKING, THE VALUES DO NOT MAP AFTER EVERY TURN