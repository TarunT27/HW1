"""
Program 62: Filter dictionary entries based on their values
This program keeps only entries matching a condition.
"""

def filter_by_value(d, condition):
    """Filter dictionary by value condition"""
    filtered = {}
    for key, value in d.items():
        if condition(value):
            filtered[key] = value
    return filtered


# Main program
if __name__ == "__main__":
    test_dict = {'a': 10, 'b': 25, 'c': 5, 'd': 30, 'e': 15}
    
    print("Dictionary Value Filter")
    print("-" * 40)
    
    # Filter for values > 15
    result1 = filter_by_value(test_dict, lambda x: x > 15)
    print(f"Original: {test_dict}")
    print(f"Values > 15: {result1}\n")
    
    # Filter for even values
    result2 = filter_by_value(test_dict, lambda x: x % 2 == 0)
    print(f"Even values: {result2}\n")
    
    # Filter for values < 20
    result3 = filter_by_value(test_dict, lambda x: x < 20)
    print(f"Values < 20: {result3}")

"""
OUTPUT:
Dictionary Value Filter
----------------------------------------
Original: {'a': 10, 'b': 25, 'c': 5, 'd': 30, 'e': 15}
Values > 15: {'b': 25, 'd': 30}

Even values: {'a': 10, 'c': 5, 'd': 30}

Values < 20: {'a': 10, 'c': 5, 'e': 15}
"""
