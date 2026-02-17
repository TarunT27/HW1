"""
Program 53: Check if a key exists in a dictionary
This program validates key presence in dictionaries.
"""

def key_exists(d, key):
    """Check if key exists in dictionary"""
    return key in d


# Main program
if __name__ == "__main__":
    test_dict = {'name': 'John', 'age': 30, 'city': 'NYC'}
    test_keys = ['name', 'country', 'age', 'address']
    
    print("Dictionary Key Existence Checker")
    print("-" * 40)
    print(f"Dictionary: {test_dict}\n")
    for key in test_keys:
        exists = key_exists(test_dict, key)
        print(f"Key '{key}' exists -> {exists}")

"""
OUTPUT:
Dictionary Key Existence Checker
----------------------------------------
Dictionary: {'name': 'John', 'age': 30, 'city': 'NYC'}

Key 'name' exists -> True
Key 'country' exists -> False
Key 'age' exists -> True
Key 'address' exists -> False
"""
