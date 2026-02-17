"""
Program 112: Print the sum of all even numbers up to n using a loop
This program sums even numbers.
"""

def sum_evens_up_to(n):
    """Sum all even numbers up to n"""
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total


# Main program
if __name__ == "__main__":
    test_nums = [10, 20, 5, 100]
    
    print("Even Numbers Sum Calculator")
    print("-" * 40)
    for n in test_nums:
        total = sum_evens_up_to(n)
        print(f"Sum of evens up to {n} = {total}")

"""
OUTPUT:
Even Numbers Sum Calculator
----------------------------------------
Sum of evens up to 10 = 30
Sum of evens up to 20 = 110
Sum of evens up to 5 = 6
Sum of evens up to 100 = 2550
"""
