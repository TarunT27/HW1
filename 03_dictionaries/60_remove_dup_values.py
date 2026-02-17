"""
Program 60: Remove all duplicate values from a dictionary
This program keeps only one key for each unique value.
"""

def remove_duplicate_values(d):
    """Remove duplicate values from dictionary"""
    seen_values = set()
    result = {}
    for key, value in d.items():
        if value not in seen_values:
            result[key] = value
            seen_values.add(value)
    return result


# Main program
if __name__ == "__main__":
    test_dicts = [
        {'a': 1, 'b': 1, 'c': 2, 'd': 2},
        {'x': 'apple', 'y': 'banana', 'z': 'apple'},
        {'a': 1, 'b': 2, 'c': 3},
        {},
    ]
    
    print("Duplicate Value Remover")
    print("-" * 40)
    for d in test_dicts:
        result = remove_duplicate_values(d)
        print(f"Original: {d}")
        print(f"Result: {result}\n")

"""
OUTPUT:
Duplicate Value Remover
----------------------------------------
Original: {'a': 1, 'b': 1, 'c': 2, 'd': 2}
Result: {'a': 1, 'c': 2}

Original: {'x': 'apple', 'y': 'banana', 'z': 'apple'}
Result: {'x': 'apple', 'y': 'banana'}

Original: {'a': 1, 'b': 2, 'c': 3}
Result: {'a': 1, 'b': 2, 'c': 3}

Original: {}
Result: {}
"""
