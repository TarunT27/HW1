"""
Program 168: Rotate list by k positions
This program rotates a list to the right by k positions.
"""

def rotate_list(lst, k):
    """Rotate list by k positions"""
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),
        (['a', 'b', 'c'], 1),
        ([1, 2, 3], 5),
    ]
    
    print("List Rotator")
    print("-" * 40)
    for lst, k in test_cases:
        result = rotate_list(lst, k)
        print(f"List: {lst}, k: {k}")
        print(f"Rotated: {result}\n")

"""
OUTPUT:
List Rotator
----------------------------------------
List: [1, 2, 3, 4, 5], k: 2
Rotated: [4, 5, 1, 2, 3]

List: ['a', 'b', 'c'], k: 1
Rotated: ['c', 'a', 'b']

List: [1, 2, 3], k: 5
Rotated: [2, 3, 1]
"""
