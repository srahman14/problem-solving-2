# Constraints: n >= 10,000

# n = int(input("Enter the number n 2-10,000:  "))
n = 30

# # base case:
# if n == 2 or n == 3:
#     return n

# Generating a list of Prime Numbers
list_int = [i for i in range(2, n + 1)]
i = 0
# Using a while loop is more optimum than a for loop as 
# updating the list while in a for loop affects the index
# as the length of the list is changing after every iteration
while i < len(list_int):
    # Set the first value in the list as p to mark all its primes
    p = list_int[i]

    # Filter out the numbers which are multiples of p (and p itself)
    list_int = [j for j in list_int if j == p or j % p != 0]
    i += 1 

# Prime factorisation

def primeFactorisation(n):
    prime_factors = {}
    for i in list_int:
        if n % i != 0:
            continue
        count = 0
        while n % i == 0:
            n = n // i
            count += 1 
        prime_factors[i] = count
        if n == 1:
            break
    results = []
    for i in prime_factors:
        if prime_factors[i] > 1:
            results.extend((str(i)) * prime_factors[i])
        else:
            results.extend(str(i))

    return " x ".join(results)
print(primeFactorisation(10000))