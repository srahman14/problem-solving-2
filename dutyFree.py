# 125 BAHT
leftOverMoney = (3*5) + (4*10) + (5*2) + (3*20)
# Define three vars X, Y, Z to go through all combinations to find the most optimum solution
def dutyFree():
    total_THB = leftOverMoney
    bestSolution = None
    # Used to track the solution
    minLeftOver = total_THB

    # The range here is the maximum amount of chocolate options that can be bought
    for x in range(total_THB // 10 + 1):
        for y in range(total_THB // 5):
            for z in range(total_THB // 2 + 1):
                # Where x is toblerone, y is lindt, and z is kit-kats
                # And the corresopnding cost for each chocolate
                cost = (x * 10) + (y * 5) + (z * 2)

                # If the total cost is equal to the total money, then the best solution is found
                # as no money is left to spend
                if cost == total_THB: 
                    return f"Toblerone: {x}, Lindt Lindor: {y}, Kit Kat: {z}, leftover: 0"
                # Otherwise, the cost is not exactly equal to the total cost, then track the heuristic
                # solution
                elif cost < total_THB:
                    leftover = total_THB - cost
                    if leftover < minLeftOver:
                        # The minimum leftoever for the heuristic solution
                        minLeftOver = leftover
                        bestSolution = f"Toblerone: {x}, Lindt Lindor: {y}, Kit Kat: {z}, leftover: 0"

    return bestSolution if bestSolution else "No solution found"

print(dutyFree())