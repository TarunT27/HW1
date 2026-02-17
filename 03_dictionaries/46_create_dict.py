"""
Program 46: Create a dictionary from two lists (keys and values)
This program zips keys and values into a dictionary.
"""

def create_dict(keys, values):
    """Create dictionary from two lists"""
    result = {}
    for i in range(min(len(keys), len(values))):
        result[keys[i]] = values[i]
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        (['a', 'b', 'c'], [1, 2, 3]),
        ([1, 2, 3], ['x', 'y', 'z']),
        (['name', 'age'], ['John', 30]),
        ([], []),
        (['extra_key'], [1, 2, 3])
    ]
    
    print("Dictionary Creator from Lists")
    print("-" * 40)
    for keys, values in test_cases:
        result = create_dict(keys, values)
        print(f"Keys: {keys}")
        print(f"Values: {values}")
        print(f"Result: {result}\n")

"""
OUTPUT:
Dictionary Creator from Lists
----------------------------------------
Keys: ['a', 'b', 'c']
Values: [1, 2, 3]
Result: {'a': 1, 'b': 2, 'c': 3}

Keys: [1, 2, 3]
Values: ['x', 'y', 'z']
Result: {1: 'x', 2: 'y', 3: 'z'}

Keys: ['name', 'age']
Values: ['John', 30]
Result: {'name': 'John', 'age': 30}

Keys: []
Values: []
Result: {}

Keys: ['extra_key']
Values: [1, 2, 3]
Result: {'extra_key': 1}
"""
