chocolateOptions = {
    "Kit Kat": 2,
    "Lindt Lindor": 5,
    "Toblerone": 10
}

# 125 BAHT
leftOverMoney = (3*5) + (4*10) + (5*2) + (3*20)

# Define three vars X, Y, Z to find all combinations
def dutyFree():
    total_THB = leftOverMoney
    bestSolution = None
    # Used to track the heuristic solution
    minLeftOver = total_THB

    for x in range(total_THB // chocolateOptions["Toblerone"] + 1):
        for y in range(total_THB // chocolateOptions["Lindt Lindor"]):
            for z in range(total_THB // chocolateOptions["Kit Kat"] + 1):
                cost = x * chocolateOptions["Toblerone"] + y * chocolateOptions["Lindt Lindor"] + z * chocolateOptions["Kit Kat"]

                if cost == total_THB: # Best Solution
                    return f"Toblerone: {x}, Lindt Lindor: {y}, Kit Kat: {z}, leftover: 0"
                elif cost < total_THB:
                    leftover = total_THB - cost
                    if leftover < minLeftOver:
                        minLeftOver = leftover
                        bestSolution = f"Toblerone: {x}, Lindt Lindor: {y}, Kit Kat: {z}, leftover: 0"

    return bestSolution if bestSolution else "No solution found"

print(dutyFree())