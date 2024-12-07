# The Rules of Life:
# 1. Any live cell with fewer than two live neighbours die. This is called underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation. This is called
# stable population.
# 3. Any live cell with more than three live neighbours dies. This is called overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell. This is called
# reproduction.

import numpy as np
import time

# grid = np.full((6, 6), 0)
grid = np.array([
    [0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0]
])
coordinates = []
round = 0

while True:
    coordinateInput = input("Enter x, y coordinates (row, col) or 'q' to quit: ")

    if coordinateInput.lower().strip() == 'q':
        break

    try:
        x, y = map(int, coordinateInput.split())
        x, y = x - 1, y - 1

        if not (0 <= x < 6 and 0 <= y < 6):
            print("Coordinates must be between 1 and 6")
            continue

        if grid[x][y] == 1:
            print("This is already a live cell!")
            continue

        grid[x][y] = 1
        coordinates.append((x, y))
    except ValueError:
        print("Invalid input! Please enter two numbers separted by a space or 'q' to quit")
    
# print(grid)

def countNeighbours(grid, x, y):
    # Defining the relative positions for the eight neighbours
    # Around the cell
    count = 0
    neighbours = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),            (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for dx, dy in neighbours:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            count += grid[nx][ny]
    
    return count

def ruleOne(grid):
    newGrid = np.copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                live_neighbours = countNeighbours(grid, i, j)
                if live_neighbours < 2:
                    newGrid[i][j] = 0
                    print(f"Cell ({i + 1}, {j + 1}) dies due to underpopulation")
    return newGrid
    
def ruleTwo(grid):
    newGrid = np.copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                live_neighbours = countNeighbours(grid, i, j)
                if live_neighbours == 2 or live_neighbours == 3:
                    print(f"Cell ({i + 1}, {j + 1}) lives due to stable population")
                else:
                    newGrid[i][j] = 0
                    print(f"Cell ({i + 1}, {j + 1}) dies due to lack of stable population")
    return newGrid

def ruleThree(grid):
    newGrid = np.copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                live_neighbours = countNeighbours(grid, i, j)
                if live_neighbours > 3:
                    newGrid[i][j] = 0
                    print(f"Cell ({i + 1}, {j + 1}) dies due to overpopulation")
    return newGrid

def ruleFour(grid):
    newGrid = np.copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                live_neighbours = countNeighbours(grid, i, j)
                if live_neighbours == 3:
                    newGrid[i][j] = 1
                    print(f"Cell ({i + 1}, {j + 1}) reproduces")
    return newGrid

# Run the game of life for multiple iterations
for generation in range(10):  # Adjust the number of generations as needed
    print(f"\nGeneration {generation + 1}:")
    grid = ruleOne(grid)  
    grid = ruleTwo(grid)  
    grid = ruleThree(grid)  
    grid = ruleFour(grid)  
    print(grid)
    time.sleep(1)  # Pause for 1 second between generations (optional)
