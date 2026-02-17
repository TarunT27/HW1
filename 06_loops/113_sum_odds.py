"""
Program 113: Print the sum of all odd numbers up to n using a loop
This program sums odd numbers.
"""

def sum_odds_up_to(n):
    """Sum all odd numbers up to n"""
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total


# Main program
if __name__ == "__main__":
    test_nums = [10, 20, 5, 100]
    
    print("Odd Numbers Sum Calculator")
    print("-" * 40)
    for n in test_nums:
        total = sum_odds_up_to(n)
        print(f"Sum of odds up to {n} = {total}")

"""
OUTPUT:
Odd Numbers Sum Calculator
----------------------------------------
Sum of odds up to 10 = 25
Sum of odds up to 20 = 100
Sum of odds up to 5 = 9
Sum of odds up to 100 = 2500
"""
