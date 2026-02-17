"""
Program 61: Get the key with the maximum value in a dictionary
This program finds the key associated with largest value.
"""

def key_with_max_value(d):
    """Get key with maximum value in dictionary"""
    if not d:
        return None
    max_key = None
    max_value = None
    for key, value in d.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
    return max_key


# Main program
if __name__ == "__main__":
    test_dicts = [
        {'a': 5, 'b': 2, 'c': 8, 'd': 1},
        {'x': 100, 'y': 50, 'z': 75},
        {'name': 'John'},
        {},
    ]
    
    print("Max Value Key Finder")
    print("-" * 40)
    for d in test_dicts:
        key = key_with_max_value(d)
        print(f"{d}")
        print(f"Key with max value: {key}\n")

"""
OUTPUT:
Max Value Key Finder
----------------------------------------
{'a': 5, 'b': 2, 'c': 8, 'd': 1}
Key with max value: c

{'x': 100, 'y': 50, 'z': 75}
Key with max value: x

{'name': 'John'}
Key with max value: name

{}
Key with max value: None
"""
