"""
Program 101: Print all prime numbers between 1 and 100 using a loop
This program generates list of primes.
"""

def is_prime(num):
    """Check if number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes_up_to(limit):
    """Get all primes up to limit"""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Main program
if __name__ == "__main__":
    print("Prime Numbers between 1 and 100")
    print("-" * 40)
    primes = primes_up_to(100)
    print(primes)

"""
OUTPUT:
Prime Numbers between 1 and 100
----------------------------------------
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
