"""
Program 56: Get a list of all keys and values in a dictionary
This program extracts keys and values separately.
"""

def get_keys_and_values(d):
    """Get all keys and values from dictionary"""
    keys = []
    values = []
    for key in d:
        keys.append(key)
        values.append(d[key])
    return keys, values


# Main program
if __name__ == "__main__":
    test_dicts = [
        {'a': 1, 'b': 2, 'c': 3},
        {'name': 'John', 'age': 30},
        {},
    ]
    
    print("Keys and Values Extractor")
    print("-" * 40)
    for d in test_dicts:
        keys, values = get_keys_and_values(d)
        print(f"Dictionary: {d}")
        print(f"Keys: {keys}")
        print(f"Values: {values}\n")

"""
OUTPUT:
Keys and Values Extractor
----------------------------------------
Dictionary: {'a': 1, 'b': 2, 'c': 3}
Keys: ['a', 'b', 'c']
Values: [1, 2, 3]

Dictionary: {'name': 'John', 'age': 30}
Keys: ['name', 'age']
Values: ['John', 30]

Dictionary: {}
Keys: []
Values: []
"""
