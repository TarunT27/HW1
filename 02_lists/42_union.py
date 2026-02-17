"""
Program 42: Find the union of two lists
This program combines all unique elements from both lists.
"""

def union(lst1, lst2):
    """Find union of two lists"""
    result = []
    seen = set()
    for item in lst1 + lst2:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [3, 4, 5]),
        ([1, 2, 2, 3], [3, 4, 4]),
        (['a', 'b'], ['b', 'c']),
        ([1, 2, 3], [1, 2, 3]),
        ([], [1, 2])
    ]
    
    print("List Union Finder")
    print("-" * 40)
    for lst1, lst2 in test_cases:
        result = union(lst1, lst2)
        print(f"{lst1} ∪ {lst2}")
        print(f"  -> {result}\n")

"""
OUTPUT:
List Union Finder
----------------------------------------
[1, 2, 3] ∪ [3, 4, 5]
  -> [1, 2, 3, 4, 5]

[1, 2, 2, 3] ∪ [3, 4, 4]
  -> [1, 2, 3, 4]

['a', 'b'] ∪ ['b', 'c']
  -> ['a', 'b', 'c']

[1, 2, 3] ∪ [1, 2, 3]
  -> [1, 2, 3]

[] ∪ [1, 2]
  -> [1, 2]
"""
