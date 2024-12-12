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

def mapping(pos, player):
    for row in matrix:
        for k in row:
            if k == pos:
                row[row.index(k)] = player

bridges = {
   4: 9,
   8: 15,
   12: 20,
   18: 30,
   24: 34,
   29: 34,
   35: 39,
   40: 50,
   46: 52,
   50: 53,
   51: 57,
}

bridgesPrev = {}

hotels = {
   10: 1,
   21: 1,
   30: 1,
   38: 1,
   45: 1,
   57: 1,
   61: 1,
}

hotelsPrev = {}

count = 1
for i in bridges:
    mapping(i, f"B{count}")
    bridgesPrev[f"B{count}"] = i
    count +=1


count = 1
for i in hotels:
    mapping(i, f"H{count}")
    hotelsPrev[f"H{count}"] = i
    count +=1

# NEED FIX
# def getBridgePrev(pos):
#     indexOfBridge = list(bridgesPrev.values()).index(pos)

#     if indexOfBridge:
#         keyBridge, valueBridge = list(bridgesPrev.items())[indexOfBridge]

#     return keyBridge

# def getHotelPrev(pos):
#     indexOfHotel= list(hotelsPrev.values()).index(pos)

#     if indexOfHotel:
#         keyHotel, valueHotel= list(hotelsPrev.items())[indexOfHotel]

#     print(valueHotel)

win = False
# For hotels
skippedTurnOne = False
skippedTurnTwo = False

playerOnePos = 1
playerTwoPos = 1
previousPositionOne = 0
previousPositionTwo = 0

# while not win:
#     time.sleep(1)
#     if previousPositionOne != 0:
#        mapping("P1", previousPositionOne)
#        previousPositionOne = 0
#     if previousPositionTwo != 0:
#        mapping("P2", previousPositionTwo)
#        previousPositionTwo = 0
    
#     if playerOnePos in hotels and skippedTurnOne != False:
#        print("Player 1 turn skipped!")
#        skippedTurnOne = False
#     else:
#         diceRollOne = random.randint(1, 6)
#         print("Player 1 Turn: \n")
#         input("Enter to roll the dice! ")
#         print("Dice roll: ", end =" ")
#         time.sleep(3)
#         print(diceRollOne)
#         playerOnePos += diceRollOne
#         previousPositionOne = playerOnePos
#         print(f"Player one score: {playerOnePos}")

#     if playerTwoPos in hotels and skippedTurnTwo != False:
#        print("Player 2 turn skipped!")
#        skippedTurnTwo = False
#     else:
#         diceRollTwo = random.randint(1, 6)
#         print("Player 2 Turn: \n")
#         input("Enter to roll the dice! ")
#         print("Dice roll: ", end =" ")
#         time.sleep(3)
#         print(diceRollTwo)
#         playerTwoPos += diceRollTwo
#         previousPositionTwo  = playerTwoPos
#         print(f"Player tow score: {playerTwoPos}")
    
# NEED TO CHECK FOR B1/H1 for example to MAP correctly
#     bridgePrevOne = getBridgePrev(playerOnePos)
#     bridgePrevTwo = getBridgePrev(playerTwoPos)
#     hotelPrevOne = getHotelPrev(playerOnePos)
#     hotelPrevTwo = getHotelPrev(playerTwoPos)

#     if (playerOnePos in hotels):
#        skippedTurnOne = True
#     if (playerTwoPos in hotels):
#        skippedTurnTwo = True

#     if playerOnePos == playerTwoPos:
#        mapping(playerOnePos, "P1/2")
#     else:
#        mapping(playerTwoPos, "P2")
#        mapping(playerOnePos, "P1") 


#     time.sleep(2)
#     print("Game of Goose: \n")
#     time.sleep(2)
#     showBoard(size)

# result = mapping(1)

# print(result)

