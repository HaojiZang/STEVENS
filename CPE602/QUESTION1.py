def is_prime(n):
    """
    Give a positive integer, determine whether it is prime using trial division
    """
    # 1 and numbers less than 1 are not prime
    if n <= 1:
        return False
    
    # Trial division
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If no divisors are found, n is prime
    return True

# Main print
number = int(input("Enter a positive integer: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
