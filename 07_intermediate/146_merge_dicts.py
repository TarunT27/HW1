"""
Program 146: Merge multiple dictionaries into one
This program combines multiple dictionaries into a single dictionary.
"""

def merge_dictionaries(*dicts):
    """Merge multiple dictionaries"""
    result = {}
    for d in dicts:
        result.update(d)
    return result


# Main program
if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict3 = {'e': 5, 'f': 6}
    
    print("Merge Multiple Dictionaries")
    print("-" * 40)
    print(f"Dict1: {dict1}")
    print(f"Dict2: {dict2}")
    print(f"Dict3: {dict3}")
    
    merged = merge_dictionaries(dict1, dict2, dict3)
    print(f"Merged: {merged}")

"""
OUTPUT:
Merge Multiple Dictionaries
----------------------------------------
Dict1: {'a': 1, 'b': 2}
Dict2: {'c': 3, 'd': 4}
Dict3: {'e': 5, 'f': 6}
Merged: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
"""
