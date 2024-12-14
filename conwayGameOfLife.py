# The Rules of Life:
# 1. Any live cell with fewer than two live neighbours die. This is called underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation. This is called
# stable population.
# 3. Any live cell with more than three live neighbours dies. This is called overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell. This is called
# reproduction.

import numpy as np
import time

# Using numpy, I quickly create a matrix of zeroes
# I use the first 2 parameters for .full(), shape and fill
# shape defined as 6x6 and fill = 0   
grid = np.full((6, 6), 0)

# Test grid - used for debugging
# grid = np.array([
#     [0, 0, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0],
#     [0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0]
# ])

# Useful to hold coordinates for error-checking
# i.e. validating coordinate inputs already in the grid
coordinates = []

while True:
    coordinateInput = input(
        "Enter x, y coordinates (row, col) or 'q' to quit: ")
    # Base case if user wants to quit it is the first thing checked at every
    # iteration, so user will quit immediately
    if coordinateInput.lower().strip() == 'q':
        break
    
    # Try-except catch used to handle invalid user inputs
    try:
        # Parse the uesr input into two intergers => x, y
        # i.e. input => 1 3 => x, y = 1, 3
        x, y = map(int, coordinateInput.split())
        # Subtract x and y by 1, for indexing of grid (zero-based)
        x, y = x - 1, y - 1

        # Bounds for x, y checked, if x or y not between 1-6 skip rest of code on
        # to next iteration
        if not (0 <= x < 6 and 0 <= y < 6):
            print("Coordinates must be between 1 and 6")
            continue
        
        # If a cell is alraedy live, then rest of iteration skipped onto next iteration
        if grid[x][y] == 1:
            print("This is already a live cell!")
            continue
        
        # If none of these if-statements are true, then set x, y coordinates as a live cell
        grid[x][y] = 1
        coordinates.append((x, y))
    # If an invalid input is put in, i.e. not intergers, error is thrown to let the user now
    # or further no space is placed between the intergers
    except ValueError:
        print("Invalid input! Please enter two numbers separted by a space or 'q' to quit")


def countNeighbours(grid, x, y):
    # Defining the relative positions around the current cell for the eight possible neighbours
    neighbours = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    # Used to track the count of live neighbours
    count = 0

    for xPos, yPos in neighbours:
        # This is to calculate the coordinates around the cell
        # i.e. [-1, -1] + [2, 1] = [1, 0] => gives the top-left cell
        # Using this logic, i can check for live neighbours
        xCoord, yCoord = x + xPos, y + yPos
        # Check for if the x-coordinate and y-coordinate is in bounds
        if 0 <= xCoord < len(grid) and 0 <= yCoord < len(grid[0]):
            # if the neighbour of the cell is live is live then increment the count
            if grid[xCoord][yCoord] == 1:
                count += 1
                
    return count


def applyRules(grid):
    # using .shape to set the bounds for rows and columns
    # i.e. rows, cols = (6, 6)
    rows, cols = grid.shape
    # Use of a copy of the original grid, is to ensure all rules
    # apply to the original grid's states, preventing changes in one cell from
    # affecting the compuation of other cells in the same round/generation
    newGrid = np.copy(grid)

    for i in range(rows):
        for j in range(cols):
            live_neighbours = countNeighbours(grid, i, j)

            if grid[i][j] == 1:
                # Rule one: underpopulation
                # If number of live cells around the cell is less than 2, rule 1 applies
                if live_neighbours < 2:
                    newGrid[i][j] = 0
                    print(f"Cell ({i + 1}, {j + 1}) dies due to underpopulation")
                # Rule three: overpopulation
                # If number of live cells around the cell is greater than 3, rule 3 applies
                elif live_neighbours > 3:
                    newGrid[i][j] = 0
                    print(f"Cell ({i + 1}, {j + 1}) dies due to overpopulation")
                # Rule 2 is implied by the failure of rule 1 and rule 3 here, if these rules do not apply,
                # then rule 2 will naturally follow as:
                # Any live cell with two or three live neighbours lives on to the next generation.
            elif grid[i][j] == 0:
                # Rule four: reproduction
                # If number of live cells around the cell is exactly 3, rule 4 applies
                if live_neighbours == 3:
                    newGrid[i][j] = 1
                    print(f"Cell ({i + 1}, {j + 1}) reproduces")

    return newGrid

# Used to display the grid by converting each cell into a string first to use the .join() function
def displayGrid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print("\nActivity:")

round = 1
# Main loop
while True:#
    print(f"Round {round}:")
    time.sleep(0.8)
    displayGrid(grid)
    time.sleep(2)
    grid = applyRules(grid)
    round += 1
    time.sleep(1.6)
    userInput = input("\nPress enter to continue to next round or 'q' to quit: ")

    if userInput.lower().strip() == 'q':
        print("Simulation quit.")
        break
