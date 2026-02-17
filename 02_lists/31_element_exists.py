"""
Program 31: Check if an element exists in a list
This program checks if a specific value is in the list.
"""

def element_exists(lst, element):
    """Check if element exists in list"""
    for item in lst:
        if item == element:
            return True
    return False


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([10, 20, 30], 15),
        (['a', 'b', 'c'], 'b'),
        ([], 1),
        ([None, 0, False], None)
    ]
    
    print("Element Existence Checker")
    print("-" * 40)
    for lst, element in test_cases:
        exists = element_exists(lst, element)
        print(f"{element} in {lst} -> {exists}")

"""
OUTPUT:
Element Existence Checker
----------------------------------------
3 in [1, 2, 3, 4, 5] -> True
15 in [10, 20, 30] -> False
b in ['a', 'b', 'c'] -> True
1 in [] -> False
None in [None, 0, False] -> True
"""
