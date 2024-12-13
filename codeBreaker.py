# Constraints: n <= 10,000

# n = int(input("Enter the number n 2-10,000:  "))
n = 3999

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
    # Necessary to use a dictionary so I can attach the number of times
    # a prime factor is counted and then produce it after in a format
    # desired
    prime_factors = {}
    for i in list_int:
        # if the current number in list cannot divide into the current 
        # value of N, skip to the next value  
        if n % i != 0:
            continue
        # Hold the number of times that the current prime goes into N, 
        count = 0
        # The loop will automatically break out after the prime no longer
        # divides into N
        while n % i == 0:
            n = n // i
            count += 1 
        # Attach the number of times the prime goes into N in the dictionary
        prime_factors[i] = count
        # I.e. N can no longer be divided down anymore
        if n == 1:
            break
    
    results = []
    print(prime_factors)
    for i in prime_factors:
        # if the prime factor has more than one digit, it has to be handled using
        # .append() so that it's whole value is appended, i.e. if a prime factor was
        # 43, using .append() => '43', where as using .extend() => '4', '3'
        # .extend() is useful where needed to repeat a prime factor, i.e. if a prime
        # factor such as 2 was repeated 5 times, .append() => '22222', where as using
        # .extend() => '2', '2', '2', '2', '2'

        # Checking if a prime factor has more than one digit
        if len(str(i)) > 1:
            # Checking the number of times the prime factor is repeated and adding it 
            # to the list that many times
            if prime_factors[i] > 1:
                results.append(str(i) * prime_factors[i])
            else:
                # If only repeated once only added once
                results.append(str(i))

        # Checking for prime factors of only one digit
        elif prime_factors[i] > 1:
            # Add the prime factors for the number of times that it divided into N
            # to the results list
            results.extend((str(i)) * prime_factors[i])
        else:
            # If it only divided into N once, it is only added once
            results.extend(str(i))
    # Final results separated by 'x' using .join()
    print(results)
    return " x ".join(results)

result = primeFactorisation(n)
print(result)

