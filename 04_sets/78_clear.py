"""
Program 78: Remove all elements from a set
This program clears a set completely.
"""

def clear_set(s):
    """Remove all elements from a set"""
    s.clear()
    return s


# Main program
if __name__ == "__main__":
    test_sets = [
        {1, 2, 3, 4, 5},
        {'a', 'b', 'c'},
        {1},
        set(),
    ]
    
    print("Set Clearer")
    print("-" * 40)
    for s in test_sets:
        original = s.copy()
        cleared = clear_set(s)
        print(f"Original: {original}")
        print(f"After clear: {cleared}\n")

"""
OUTPUT:
Set Clearer
----------------------------------------
Original: {1, 2, 3, 4, 5}
After clear: set()

Original: {'a', 'b', 'c'}
After clear: set()

Original: {1}
After clear: set()

Original: set()
After clear: set()
"""
