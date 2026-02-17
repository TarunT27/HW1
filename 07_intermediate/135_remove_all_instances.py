"""
Program 135: Remove all occurrences of a specific element from a list
This program removes all instances of an element.
"""

def remove_all_instances(lst, target):
    """Remove all occurrences of target"""
    return [x for x in lst if x != target]


# Main program
if __name__ == "__main__":
    test_cases = [([1, 2, 2, 3, 2, 4], 2), (['a', 'b', 'a'], 'a')]
    
    print("Element Remover (all)")
    print("-" * 40)
    for lst, target in test_cases:
        result = remove_all_instances(lst, target)
        print(f"{lst} remove {target} -> {result}")

"""
OUTPUT:
Element Remover (all)
----------------------------------------
[1, 2, 2, 3, 2, 4] remove 2 -> [1, 3, 4]
['a', 'b', 'a'] remove a -> ['b']
"""
