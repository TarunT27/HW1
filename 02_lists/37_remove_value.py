"""
Program 37: Remove all occurrences of a value from a list
This program removes every instance of a specified element.
"""

def remove_all_occurrences(lst, value):
    """Remove all occurrences of a value from list"""
    result = []
    for item in lst:
        if item != value:
            result.append(item)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 2, 4, 2], 2),
        ([5, 5, 5, 5], 5),
        ([1, 2, 3, 4, 5], 0),
        (['a', 'b', 'a', 'c'], 'a'),
        ([], 1)
    ]
    
    print("Value Remover")
    print("-" * 40)
    for lst, value in test_cases:
        result = remove_all_occurrences(lst, value)
        print(f"{lst} -> Remove {value} -> {result}")

"""
OUTPUT:
Value Remover
----------------------------------------
[1, 2, 3, 2, 4, 2] -> Remove 2 -> [1, 3, 4]
[5, 5, 5, 5] -> Remove 5 -> []
[1, 2, 3, 4, 5] -> Remove 0 -> [1, 2, 3, 4, 5]
['a', 'b', 'a', 'c'] -> Remove a -> ['b', 'c']
[] -> Remove 1 -> []
"""
