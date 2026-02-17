"""
Program 100: Count even numbers in a list using a loop
This program counts even elements.
"""

def count_evens(lst):
    """Count even numbers in list"""
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5, 6],
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [],
        [0, 2, 4]
    ]
    
    print("Even Number Counter")
    print("-" * 40)
    for lst in test_lists:
        count = count_evens(lst)
        print(f"{lst} -> Even count: {count}")

"""
OUTPUT:
Even Number Counter
----------------------------------------
[1, 2, 3, 4, 5, 6] -> Even count: 3
[1, 3, 5, 7] -> Even count: 0
[2, 4, 6, 8] -> Even count: 4
[] -> Even count: 0
[0, 2, 4] -> Even count: 3
"""
