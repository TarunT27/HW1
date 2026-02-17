"""
Program 55: Invert a dictionary (swap keys and values)
This program reverses keys and values.
"""

def invert_dictionary(d):
    """Invert dictionary - swap keys and values"""
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted


# Main program
if __name__ == "__main__":
    test_dicts = [
        {'a': 1, 'b': 2, 'c': 3},
        {'name': 'John', 'city': 'NYC'},
        {'x': 'apple', 'y': 'banana'},
        {},
    ]
    
    print("Dictionary Inverter")
    print("-" * 40)
    for d in test_dicts:
        inverted = invert_dictionary(d)
        print(f"Original: {d}")
        print(f"Inverted: {inverted}\n")

"""
OUTPUT:
Dictionary Inverter
----------------------------------------
Original: {'a': 1, 'b': 2, 'c': 3}
Inverted: {1: 'a', 2: 'b', 3: 'c'}

Original: {'name': 'John', 'city': 'NYC'}
Inverted: {'John': 'name', 'NYC': 'city'}

Original: {'x': 'apple', 'y': 'banana'}
Inverted: {'apple': 'x', 'banana': 'y'}

Original: {}
Inverted: {}
"""
