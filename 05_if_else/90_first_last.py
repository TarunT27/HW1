"""
Program 90: Check if first and last elements of a list are the same
This program compares list boundaries.
"""

def first_last_same(lst):
    """Check if first and last elements are same"""
    if len(lst) == 0:
        return "Empty list"
    elif lst[0] == lst[-1]:
        return True
    else:
        return False


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 1],
        [5, 4, 3, 5],
        [1, 2, 3, 4],
        [1],
        [],
        ['a', 'b', 'a']
    ]
    
    print("First/Last Element Checker")
    print("-" * 40)
    for lst in test_lists:
        result = first_last_same(lst)
        print(f"{lst} -> {result}")

"""
OUTPUT:
First/Last Element Checker
----------------------------------------
[1, 2, 3, 1] -> True
[5, 4, 3, 5] -> True
[1, 2, 3, 4] -> False
[1] -> True
[] -> Empty list
['a', 'b', 'a'] -> True
"""
