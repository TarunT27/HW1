"""
Program 47: Access a value by key in a dictionary
This program retrieves values using dictionary keys.
"""

def access_value(d, key):
    """Access value by key in dictionary"""
    if key in d:
        return d[key]
    else:
        return None


def access_value_safe(d, key, default=None):
    """Access value safely with default"""
    return d.get(key, default)


# Main program
if __name__ == "__main__":
    test_dict = {'name': 'John', 'age': 30, 'city': 'NYC'}
    test_keys = ['name', 'age', 'country', 'city']
    
    print("Dictionary Value Accessor")
    print("-" * 40)
    print(f"Dictionary: {test_dict}\n")
    for key in test_keys:
        value = access_value_safe(test_dict, key, 'Not Found')
        print(f"Key '{key}' -> {value}")

"""
OUTPUT:
Dictionary Value Accessor
----------------------------------------
Dictionary: {'name': 'John', 'age': 30, 'city': 'NYC'}

Key 'name' -> John
Key 'age' -> 30
Key 'country' -> Not Found
Key 'city' -> NYC
"""
