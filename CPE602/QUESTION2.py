def prime_factors(n):
    """
    Given a positive integer, find the prime factorization of this integer
    """
    factors = []  # List of prime number
    divisor = 2  # The smallest prime number

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor  # Divide n 
        divisor += 1  # Move to the next

        # Stop when divisor exceeds the square root of n
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break

    return factors

# Main print
number = int(input("Enter a positive integer: "))
if number > 0:
    print(f"The prime factorization of {number} is: {prime_factors(number)}")
else:
    print("Please enter a positive integer.")
