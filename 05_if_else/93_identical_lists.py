"""
Program 93: Check if two lists are identical
This program compares list equality.
"""

def lists_identical(lst1, lst2):
    """Check if two lists are identical"""
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 4]),
        (['a', 'b'], ['a', 'b']),
        ([], []),
        ([1], [1, 2])
    ]
    
    print("List Identity Checker")
    print("-" * 40)
    for lst1, lst2 in test_cases:
        result = lists_identical(lst1, lst2)
        print(f"{lst1} == {lst2} -> {result}")

"""
OUTPUT:
List Identity Checker
----------------------------------------
[1, 2, 3] == [1, 2, 3] -> True
[1, 2, 3] == [1, 2, 4] -> False
['a', 'b'] == ['a', 'b'] -> True
[] == [] -> True
[1] == [1, 2] -> False
"""
