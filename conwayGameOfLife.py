# The Rules of Life:
# 1. Any live cell with fewer than two live neighbours die. This is called underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation. This is called
# stable population.
# 3. Any live cell with more than three live neighbours dies. This is called overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell. This is called
# reproduction.

import numpy as np

grid = np.full((6, 6), 0)

print(grid)

while True:
    x, y = map(int, input("Enter your x, y coordinate (row, col)").split())
    x, y = x - 1, y - 1

    grid[x][y] = 1

    if x or y == -1:
        break

print(grid)