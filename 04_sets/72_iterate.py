"""
Program 72: Iterate over the elements of a set
This program demonstrates iterating through set elements.
"""

def iterate_set(s):
    """Iterate over set elements"""
    for item in s:
        print(f"Element: {item}")


# Main program
if __name__ == "__main__":
    test_sets = [
        {1, 2, 3, 4, 5},
        {'a', 'b', 'c'},
        {10},
        set(),
    ]
    
    print("Set Iterator")
    print("-" * 40)
    for s in test_sets:
        print(f"Set: {s}")
        iterate_set(s)
        print()

"""
OUTPUT:
Set Iterator
----------------------------------------
Set: {1, 2, 3, 4, 5}
Element: 1
Element: 2
Element: 3
Element: 4
Element: 5

Set: {'a', 'b', 'c'}
Element: a
Element: b
Element: c

Set: {10}
Element: 10

Set: set()
"""
