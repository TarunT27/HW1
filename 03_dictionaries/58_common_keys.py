"""
Program 58: Find common keys between two dictionaries
This program identifies keys present in both dictionaries.
"""

def common_keys(d1, d2):
    """Find common keys between two dictionaries"""
    common = []
    for key in d1:
        if key in d2:
            common.append(key)
    return common


# Main program
if __name__ == "__main__":
    test_cases = [
        ({'a': 1, 'b': 2, 'c': 3}, {'b': 20, 'c': 30, 'd': 40}),
        ({'x': 10, 'y': 20}, {'x': 100, 'y': 200}),
        ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}),
        ({}, {'a': 1}),
    ]
    
    print("Common Keys Finder")
    print("-" * 40)
    for d1, d2 in test_cases:
        common = common_keys(d1, d2)
        print(f"{d1}")
        print(f"{d2}")
        print(f"Common keys: {common}\n")

"""
OUTPUT:
Common Keys Finder
----------------------------------------
{'a': 1, 'b': 2, 'c': 3}
{'b': 20, 'c': 30, 'd': 40}
Common keys: ['b', 'c']

{'x': 10, 'y': 20}
{'x': 100, 'y': 200}
Common keys: ['x', 'y']

{'a': 1, 'b': 2}
{'c': 3, 'd': 4}
Common keys: []

{}
{'a': 1}
Common keys: []
"""
