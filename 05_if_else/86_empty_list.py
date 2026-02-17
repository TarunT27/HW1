"""
Program 86: Check if a list is empty or not
This program validates if a list contains elements.
"""

def is_list_empty(lst):
    """Check if list is empty"""
    if len(lst) == 0:
        return "Empty"
    else:
        return "Not Empty"


# Main program
if __name__ == "__main__":
    test_lists = [
        [],
        [1],
        [1, 2, 3],
        [None],
        [[]]
    ]
    
    print("List Empty Checker")
    print("-" * 40)
    for lst in test_lists:
        result = is_list_empty(lst)
        print(f"{lst} -> {result}")

"""
OUTPUT:
List Empty Checker
----------------------------------------
[] -> Empty
[1] -> Not Empty
[1, 2, 3] -> Not Empty
[None] -> Not Empty
[[]] -> Not Empty
"""
