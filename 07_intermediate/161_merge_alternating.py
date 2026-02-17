"""
Program 161: Merge two lists alternately
This program interleaves elements from two lists.
"""

def merge_alternating(lst1, lst2):
    """Merge lists alternately"""
    result = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        result.append(lst1[i])
        result.append(lst2[j])
        i += 1
        j += 1
    
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], ['a', 'b', 'c']),
        ([1, 2], ['a', 'b', 'c', 'd']),
    ]
    
    print("Merge Lists Alternately")
    print("-" * 40)
    for lst1, lst2 in test_cases:
        result = merge_alternating(lst1, lst2)
        print(f"List1: {lst1}, List2: {lst2}")
        print(f"Merged: {result}\n")

"""
OUTPUT:
Merge Lists Alternately
----------------------------------------
List1: [1, 2, 3], List2: ['a', 'b', 'c']
Merged: [1, 'a', 2, 'b', 3, 'c']

List1: [1, 2], List2: ['a', 'b', 'c', 'd']
Merged: [1, 'a', 2, 'b', 'c', 'd']
"""
