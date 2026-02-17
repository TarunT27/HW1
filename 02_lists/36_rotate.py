"""
Program 36: Rotate a list by a specified number of positions
This program shifts list elements by k positions.
"""

def rotate_list(lst, k):
    """Rotate a list by k positions"""
    if not lst:
        return lst
    k = k % len(lst)  # Handle k larger than list length
    return lst[-k:] + lst[:-k] if k else lst


def rotate_list_manual(lst, k):
    """Rotate list manually"""
    if not lst:
        return lst
    n = len(lst)
    k = k % n
    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = lst[i]
    return rotated


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3], 1),
        ([1, 2, 3, 4], 5),
        (['a', 'b', 'c'], 0),
        ([1], 3)
    ]
    
    print("List Rotator")
    print("-" * 40)
    for lst, k in test_cases:
        rotated = rotate_list(lst, k)
        print(f"{lst} rotated by {k} -> {rotated}")

"""
OUTPUT:
List Rotator
----------------------------------------
[1, 2, 3, 4, 5] rotated by 2 -> [4, 5, 1, 2, 3]
[1, 2, 3] rotated by 1 -> [3, 1, 2]
[1, 2, 3, 4] rotated by 5 -> [4, 1, 2, 3]
['a', 'b', 'c'] rotated by 0 -> ['a', 'b', 'c']
[1] rotated by 3 -> [1]
"""
