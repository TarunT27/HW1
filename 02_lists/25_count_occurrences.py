"""
Program 25: Count the occurrences of an element in a list
This program counts how many times an element appears.
"""

def count_occurrences(lst, element):
    """Count occurrences of an element in a list"""
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 2, 4, 2], 2),
        ([5, 5, 5, 5], 5),
        ([1, 2, 3, 4], 0),
        (['a', 'b', 'a', 'c', 'a'], 'a'),
        ([], 1)
    ]
    
    print("Element Occurrence Counter")
    print("-" * 40)
    for lst, element in test_cases:
        count = count_occurrences(lst, element)
        print(f"'{element}' in {lst} -> {count} times")

"""
OUTPUT:
Element Occurrence Counter
----------------------------------------
'2' in [1, 2, 3, 2, 4, 2] -> 3 times
'5' in [5, 5, 5, 5] -> 4 times
'0' in [1, 2, 3, 4] -> 0 times
'a' in ['a', 'b', 'a', 'c', 'a'] -> 3 times
'1' in [] -> 0 times
"""
