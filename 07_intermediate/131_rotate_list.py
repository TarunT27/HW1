"""
Program 131: Rotate elements of a list by k positions
This program rotates list elements.
"""

def rotate_list(lst, k):
    """Rotate list by k positions"""
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k] if k else lst


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),
        (['a', 'b', 'c'], 1),
        ([1, 2], 3)
    ]
    
    print("List Rotator (positions)")
    print("-" * 40)
    for lst, k in test_cases:
        result = rotate_list(lst, k)
        print(f"{lst} rotated by {k} -> {result}")

"""
OUTPUT:
List Rotator (positions)
----------------------------------------
[1, 2, 3, 4, 5] rotated by 2 -> [4, 5, 1, 2, 3]
['a', 'b', 'c'] rotated by 1 -> ['c', 'a', 'b']
[1, 2] rotated by 3 -> [1, 2]
"""
