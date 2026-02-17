"""
Program 140: Find all permutations of a list
This program generates all unique permutations of elements in a list.
"""

from itertools import permutations

def list_permutations(lst):
    """Find all permutations"""
    return list(permutations(lst))


# Main program
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        ['a', 'b'],
    ]
    
    print("List Permutations Generator")
    print("-" * 40)
    for lst in test_cases:
        result = list_permutations(lst)
        print(f"List: {lst}")
        print(f"Number of permutations: {len(result)}")
        print(f"Permutations: {result}\n")

"""
OUTPUT:
List Permutations Generator
----------------------------------------
List: [1, 2, 3]
Number of permutations: 6
Permutations: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

List: ['a', 'b']
Number of permutations: 2
Permutations: [('a', 'b'), ('b', 'a')]
"""
