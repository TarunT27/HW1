"""
Program 49: Remove a key from a dictionary
This program deletes key-value pairs from dictionaries.
"""

def remove_key(d, key):
    """Remove a key from dictionary"""
    if key in d:
        del d[key]
    return d


# Main program
if __name__ == "__main__":
    test_cases = [
        ({'a': 1, 'b': 2, 'c': 3}, 'b'),
        ({'name': 'John', 'age': 30}, 'name'),
        ({'x': 1}, 'y'),
        ({}, 'key'),
    ]
    
    print("Dictionary Key Remover")
    print("-" * 40)
    for d, key in test_cases:
        original = d.copy()
        result = remove_key(d, key)
        print(f"Original: {original}")
        print(f"Removed '{key}'")
        print(f"Result: {result}\n")

"""
OUTPUT:
Dictionary Key Remover
----------------------------------------
Original: {'a': 1, 'b': 2, 'c': 3}
Removed 'b'
Result: {'a': 1, 'c': 3}

Original: {'name': 'John', 'age': 30}
Removed 'name'
Result: {'age': 30}

Original: {'x': 1}
Removed 'y'
Result: {'x': 1}

Original: {}
Removed 'key'
Result: {}
"""
