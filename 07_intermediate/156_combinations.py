"""
Program 156: Generate combinations of elements
This program creates all possible combinations of a given length from a list.
"""

from itertools import combinations

def generate_combinations(lst, r):
    """Generate combinations"""
    return list(combinations(lst, r))


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 2),
        (['a', 'b', 'c', 'd'], 2),
    ]
    
    print("Combinations Generator")
    print("-" * 40)
    for lst, r in test_cases:
        combos = generate_combinations(lst, r)
        print(f"List: {lst}, r: {r}")
        print(f"Combinations: {combos}")
        print(f"Count: {len(combos)}\n")

"""
OUTPUT:
Combinations Generator
----------------------------------------
List: [1, 2, 3], r: 2
Combinations: [(1, 2), (1, 3), (2, 3)]
Count: 3

List: ['a', 'b', 'c', 'd'], r: 2
Combinations: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
Count: 6
"""
