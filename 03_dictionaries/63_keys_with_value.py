"""
Program 63: Find keys in a dictionary that have a specific value
This program identifies all keys associated with a given value.
"""

def keys_with_value(d, target_value):
    """Find all keys with a specific value"""
    keys = []
    for key, value in d.items():
        if value == target_value:
            keys.append(key)
    return keys


# Main program
if __name__ == "__main__":
    test_cases = [
        ({'a': 1, 'b': 2, 'c': 1, 'd': 3}, 1),
        ({'name': 'John', 'city': 'NYC', 'country': 'NYC'}, 'NYC'),
        ({'x': 10, 'y': 20, 'z': 30}, 15),
        ({}, 5),
    ]
    
    print("Keys with Specific Value Finder")
    print("-" * 40)
    for d, value in test_cases:
        keys = keys_with_value(d, value)
        print(f"{d}")
        print(f"Keys with value {value}: {keys}\n")

"""
OUTPUT:
Keys with Specific Value Finder
----------------------------------------
{'a': 1, 'b': 2, 'c': 1, 'd': 3}
Keys with value 1: ['a', 'c']

{'name': 'John', 'city': 'NYC', 'country': 'NYC'}
Keys with value NYC: ['city', 'country']

{'x': 10, 'y': 20, 'z': 30}
Keys with value 15: []

{}
Keys with value 5: []
"""
