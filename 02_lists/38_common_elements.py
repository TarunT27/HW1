"""
Program 38: Find the common elements between two lists
This program identifies elements that appear in both lists.
"""

def common_elements(lst1, lst2):
    """Find common elements between two lists"""
    common = []
    for item in lst1:
        if item in lst2 and item not in common:
            common.append(item)
    return common


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [3, 4, 5, 6]),
        ([1, 1, 2, 3], [2, 3, 3, 4]),
        ([1, 2, 3], [4, 5, 6]),
        (['a', 'b', 'c'], ['b', 'c', 'd']),
        ([], [1, 2, 3])
    ]
    
    print("Common Elements Finder")
    print("-" * 40)
    for lst1, lst2 in test_cases:
        common = common_elements(lst1, lst2)
        print(f"{lst1} & {lst2}")
        print(f"  -> {common}\n")

"""
OUTPUT:
Common Elements Finder
----------------------------------------
[1, 2, 3, 4] & [3, 4, 5, 6]
  -> [3, 4]

[1, 1, 2, 3] & [2, 3, 3, 4]
  -> [2, 3]

[1, 2, 3] & [4, 5, 6]
  -> []

['a', 'b', 'c'] & ['b', 'c', 'd']
  -> ['b', 'c']

[] & [1, 2, 3]
  -> []
"""
