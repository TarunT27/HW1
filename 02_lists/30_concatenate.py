"""
Program 30: Concatenate two lists
This program combines two lists into one.
"""

def concatenate_lists(lst1, lst2):
    """Concatenate two lists"""
    return lst1 + lst2


def concatenate_lists_manual(lst1, lst2):
    """Concatenate lists manually"""
    result = []
    for item in lst1:
        result.append(item)
    for item in lst2:
        result.append(item)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [4, 5, 6]),
        (['a', 'b'], ['c', 'd']),
        ([], [1, 2, 3]),
        ([1], []),
        ([], [])
    ]
    
    print("List Concatenator")
    print("-" * 40)
    for lst1, lst2 in test_cases:
        result = concatenate_lists(lst1, lst2)
        print(f"{lst1} + {lst2} -> {result}")

"""
OUTPUT:
List Concatenator
----------------------------------------
[1, 2, 3] + [4, 5, 6] -> [1, 2, 3, 4, 5, 6]
['a', 'b'] + ['c', 'd'] -> ['a', 'b', 'c', 'd']
[] + [1, 2, 3] -> [1, 2, 3]
[1] + [] -> [1]
[] + [] -> []
"""
