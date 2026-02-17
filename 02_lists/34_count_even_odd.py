"""
Program 34: Count the number of even and odd numbers in a list
This program counts how many even and odd numbers exist.
"""

def count_even_odd(lst):
    """Count even and odd numbers in a list"""
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5, 6],
        [10, 15, 20, 25],
        [2, 4, 6, 8],
        [1, 3, 5, 7],
        []
    ]
    
    print("Even/Odd Counter")
    print("-" * 40)
    for lst in test_lists:
        even, odd = count_even_odd(lst)
        print(f"{lst}")
        print(f"  Even: {even}, Odd: {odd}\n")

"""
OUTPUT:
Even/Odd Counter
----------------------------------------
[1, 2, 3, 4, 5, 6]
  Even: 3, Odd: 3

[10, 15, 20, 25]
  Even: 2, Odd: 2

[2, 4, 6, 8]
  Even: 4, Odd: 0

[1, 3, 5, 7]
  Even: 0, Odd: 4

[]
  Even: 0, Odd: 0
"""
