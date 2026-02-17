"""
Program 41: Find the intersection of two lists
This program finds elements common to both lists.
"""

def intersection(lst1, lst2):
    """Find intersection of two lists"""
    result = []
    seen = set()
    for item in lst1:
        if item in lst2 and item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]),
        ([1, 1, 2, 2, 3], [2, 3, 3, 4]),
        (['a', 'b', 'c'], ['b', 'c', 'd']),
        ([1, 2, 3], [4, 5, 6]),
        ([], [1, 2, 3])
    ]
    
    print("List Intersection Finder")
    print("-" * 40)
    for lst1, lst2 in test_cases:
        result = intersection(lst1, lst2)
        print(f"{lst1} ∩ {lst2}")
        print(f"  -> {result}\n")

"""
OUTPUT:
List Intersection Finder
----------------------------------------
[1, 2, 3, 4, 5] ∩ [3, 4, 5, 6, 7]
  -> [3, 4, 5]

[1, 1, 2, 2, 3] ∩ [2, 3, 3, 4]
  -> [2, 3]

['a', 'b', 'c'] ∩ ['b', 'c', 'd']
  -> ['b', 'c']

[1, 2, 3] ∩ [4, 5, 6]
  -> []

[] ∩ [1, 2, 3]
  -> []
"""
