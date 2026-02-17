"""
Program 29: Check if a list is empty
This program checks if a list contains no elements.
"""

def is_list_empty(lst):
    """Check if list is empty"""
    return len(lst) == 0


def is_list_empty_manual(lst):
    """Check if list is empty without len()"""
    for _ in lst:
        return False
    return True


# Main program
if __name__ == "__main__":
    test_lists = [
        [],
        [1],
        [1, 2, 3],
        [None],
        [[]]
    ]
    
    print("Empty List Checker")
    print("-" * 40)
    for lst in test_lists:
        empty = is_list_empty(lst)
        print(f"{lst} -> Empty: {empty}")

"""
OUTPUT:
Empty List Checker
----------------------------------------
[] -> Empty: True
[1] -> Empty: False
[1, 2, 3] -> Empty: False
[None] -> Empty: False
[[]] -> Empty: False
"""
