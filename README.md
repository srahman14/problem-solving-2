# Problem Solving 2 

Problem 1: European League One
Objective: Create a Swiss Model league draw for 36 teams divided into 4 pots.

Steps to Solve:
  Display Pots: Use a nested list or dictionary to represent the four pots.
  Generate Opponents: Use Python's random module to draw two teams per pot for each team, ensuring one home and one away match.
  Track Assignments: Use a dictionary to track the assigned opponents for each team.
  User Interaction: Use input() to pause after each team's draw is displayed.
  Handle Draw Completion: Avoid assigning new matches once a team has eight opponents.
  View Draws: Allow users to query specific team assignments after all draws are complete.
  Considerations:
  
  Use functions to manage subtasks, like drawing opponents and ensuring no duplicates.
  Test for edge cases where a team already has the maximum opponents.

Problem 2: The Family
Objective: Build a family tree using dictionaries and implement functions to query relationships.

Steps to Solve: 
  Choose a Family: Select a family from fiction or history (e.g., the Stark family from Game of Thrones).
  Data Structure: Create a nested dictionary structure for the family tree.
  Functions to Implement:
  get_children(name): Return the list of children.
  get_siblings(name): Return the list of siblings.
  find_common_ancestors(name1, name2): Identify shared ancestors.
  is_related(name1, name2): Check if two people are related.
  print_family_tree(name): Recursively print the family tree starting from a person.
  Considerations:
  
  Focus on recursion for the print_family_tree function.
  Provide meaningful comments to clarify the logic of each function.
  
Problem 3: Codebreaker
Objective: Factorize a number into its prime components.

Steps to Solve:
  Prime Generation: Use the Sieve of Eratosthenes to generate all primes up to 10,000.
  Factorization: Start with the smallest prime and divide the number until it's no longer divisible. Move to the next prime.
  Output: Display the factors in the form 2x2x3x5.
  Considerations:
  
  Optimize for large inputs using a precomputed list of primes.
  Ensure correctness by testing various edge cases, like small prime numbers or large composite numbers.
  Problem 4: Duty Free
  Objective: Determine if you can spend all leftover THB on chocolates.
  
  Steps to Solve:
  
  Define Problem Variables:
  Available THB: Calculate the total THB.
  Chocolate prices: Store unit prices in a list or dictionary.
  Generate Combinations:
  Use nested loops or the itertools library to test all possible quantities of chocolates.
  Check Feasibility: For each combination, check if the total equals the available THB.
  Output Results:
  If a valid combination exists, display the quantities of each chocolate.
  Otherwise, indicate no solution is possible.
  Considerations:
  
  Optimize by stopping early when a solution is found.
  Test edge cases, such as exact matches or situations with no solution.

Problem 5: Conway’s Game of Life Simulation
This project implements Conway's Game of Life on a 6x6 grid. The simulation models the evolution of cells based on simple rules: underpopulation, stable population, overpopulation, and reproduction.

Features:
  User-defined initial state with live cell coordinates (e.g., [(1, 2), (2, 2)]).
  Displays the grid after each round and updates based on the rules of life.
  Supports a looped simulation where users press Enter to proceed or q to quit.
  Purpose: Simulates biological patterns and explores how complex systems emerge from simple rules.

Problem 6: Game of the Goose
This project is a Python implementation of the Game of the Goose, a traditional board game played on an 8x8 spiral board of 64 squares.

Features:
  Two players start at square 1 and roll dice to move towards square 64.
  Special tiles: Bridges allow shortcuts, and Hotels make players skip their turn.
  Spiral path traversal with a dynamic board reflecting the players' positions.
  Victory condition: The first player to land exactly on square 64 wins. If the dice roll overshoots, the player bounces back.
  Purpose: Provides an engaging way to simulate board game mechanics while integrating dynamic elements like bridges and hotels.
