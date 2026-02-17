"""
Program 66: Create a set and add elements to it
This program demonstrates basic set creation and addition.
"""

def create_and_add_set(elements):
    """Create a set and add elements"""
    s = set()
    for element in elements:
        s.add(element)
    return s


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c'],
        [1, 1, 2, 2, 3],
        [],
    ]
    
    print("Set Creator and Adder")
    print("-" * 40)
    for lst in test_lists:
        s = create_and_add_set(lst)
        print(f"Elements: {lst}")
        print(f"Set: {s}\n")

"""
OUTPUT:
Set Creator and Adder
----------------------------------------
Elements: [1, 2, 3, 4, 5]
Set: {1, 2, 3, 4, 5}

Elements: ['a', 'b', 'c']
Set: {'a', 'b', 'c'}

Elements: [1, 1, 2, 2, 3]
Set: {1, 2, 3}

Elements: []
Set: set()
"""
