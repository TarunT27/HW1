"""
Program 48: Update the value of a key in a dictionary
This program modifies existing dictionary values.
"""

def update_value(d, key, new_value):
    """Update value of a key in dictionary"""
    d[key] = new_value
    return d


# Main program
if __name__ == "__main__":
    test_cases = [
        ({'name': 'John', 'age': 30}, 'age', 31),
        ({'a': 1, 'b': 2}, 'c', 3),
        ({}, 'new_key', 'new_value'),
    ]
    
    print("Dictionary Value Updater")
    print("-" * 40)
    for d, key, value in test_cases:
        original = d.copy()
        updated = update_value(d, key, value)
        print(f"Original: {original}")
        print(f"Updated '{key}' to {value}")
        print(f"Result: {updated}\n")

"""
OUTPUT:
Dictionary Value Updater
----------------------------------------
Original: {'name': 'John', 'age': 30}
Updated 'age' to 31
Result: {'name': 'John', 'age': 31}

Original: {'a': 1, 'b': 2}
Updated 'c' to 3
Result: {'a': 1, 'b': 2, 'c': 3}

Original: {}
Updated 'new_key' to new_value
Result: {'new_key': 'new_value'}
"""
