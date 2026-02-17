"""
Program 150: Invert dictionary (swap keys and values)
This program creates a new dictionary with keys and values swapped.
"""

def invert_dict(d):
    """Invert dictionary"""
    return {v: k for k, v in d.items()}


# Main program
if __name__ == "__main__":
    test_cases = [
        {'a': 1, 'b': 2, 'c': 3},
        {'apple': 'red', 'banana': 'yellow'},
    ]
    
    print("Invert Dictionary")
    print("-" * 40)
    for d in test_cases:
        inverted = invert_dict(d)
        print(f"Original: {d}")
        print(f"Inverted: {inverted}\n")

"""
OUTPUT:
Invert Dictionary
----------------------------------------
Original: {'a': 1, 'b': 2, 'c': 3}
Inverted: {1: 'a', 2: 'b', 3: 'c'}

Original: {'apple': 'red', 'banana': 'yellow'}
Inverted: {'red': 'apple', 'yellow': 'banana'}
"""
