"""
Program 99: Calculate the sum of all elements in a list using a loop
This program sums list elements.
"""

def sum_list(lst):
    """Calculate sum using loop"""
    total = 0
    for num in lst:
        total += num
    return total


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [-5, 5, 0],
        [100],
        []
    ]
    
    print("List Sum Calculator")
    print("-" * 40)
    for lst in test_lists:
        total = sum_list(lst)
        print(f"{lst} -> Sum: {total}")

"""
OUTPUT:
List Sum Calculator
----------------------------------------
[1, 2, 3, 4, 5] -> Sum: 15
[10, 20, 30] -> Sum: 60
[-5, 5, 0] -> Sum: 0
[100] -> Sum: 100
[] -> Sum: 0
"""
