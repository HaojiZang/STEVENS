from itertools import combinations
from functools import reduce
from operator import mul

def count_primes_inclusion_exclusion(limit):
    """
    Find the number of primes not exceeding 10,000 using the method descibed 
    in section 8.6 to find the number of primes not excedding 100
    """
    # List of primes up to sqrt(limit) 
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    count = limit - 1

    for k in range(1, len(primes) + 1):
        # Generate combinations
        for combo in combinations(primes, k):
            # The product of primes in the combination
            product = reduce(mul, combo, 1)
            
            # The product exceeds the limit, BREAK!
            if product > limit:
                break

            # Count the multiples of the product up to the limit
            multiples = limit // product
            
            # Adjust
            if k % 2 == 1:  # Odd k -> subtract
                count -= multiples
            else:           # Even k -> add
                count += multiples

    return count

# Main print
limit = 10000
number_of_primes = count_primes_inclusion_exclusion(limit)
print(f"The number of primes not exceeding {limit} is: {number_of_primes}")