"""
Program 133: Find the intersection of two lists
This program finds common elements.
"""

def list_intersection(lst1, lst2):
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
        ([1, 2, 3, 4], [3, 4, 5]),
        (['a', 'b'], ['b', 'c'])
    ]
    
    print("List Intersection Finder")
    print("-" * 40)
    for lst1, lst2 in test_cases:
        result = list_intersection(lst1, lst2)
        print(f"{lst1} ∩ {lst2} = {result}")

"""
OUTPUT:
List Intersection Finder
----------------------------------------
[1, 2, 3, 4] ∩ [3, 4, 5] = [3, 4]
['a', 'b'] ∩ ['b', 'c'] = ['b']
"""
