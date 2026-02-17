"""
Program 67: Remove an element from a set
This program demonstrates element removal from sets.
"""

def remove_from_set(s, element):
    """Remove element from set"""
    if element in s:
        s.discard(element)
    return s


# Main program
if __name__ == "__main__":
    test_cases = [
        ({1, 2, 3, 4, 5}, 3),
        ({'a', 'b', 'c'}, 'b'),
        ({10, 20, 30}, 40),
        ({1}, 1),
    ]
    
    print("Set Element Remover")
    print("-" * 40)
    for s, element in test_cases:
        original = s.copy()
        result = remove_from_set(s, element)
        print(f"Original: {original}")
        print(f"Remove {element}: {result}\n")

"""
OUTPUT:
Set Element Remover
----------------------------------------
Original: {1, 2, 3, 4, 5}
Remove 3: {1, 2, 4, 5}

Original: {'a', 'b', 'c'}
Remove b: {'a', 'c'}

Original: {10, 20, 30}
Remove 40: {10, 20, 30}

Original: {1}
Remove 1: set()
"""
