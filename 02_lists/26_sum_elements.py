"""
Program 26: Find the sum of all elements in a list
This program calculates the total of all numbers in a list.
"""

def sum_of_elements(lst):
    """Find sum of all elements in a list"""
    total = 0
    for num in lst:
        total += num
    return total


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [-5, 0, 5],
        [100],
        []
    ]
    
    print("Sum of Elements Calculator")
    print("-" * 40)
    for lst in test_lists:
        total = sum_of_elements(lst)
        print(f"{lst} -> Sum: {total}")

"""
OUTPUT:
Sum of Elements Calculator
----------------------------------------
[1, 2, 3, 4, 5] -> Sum: 15
[10, 20, 30] -> Sum: 60
[-5, 0, 5] -> Sum: 0
[100] -> Sum: 100
[] -> Sum: 0
"""
