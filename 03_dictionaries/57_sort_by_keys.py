"""
Program 57: Sort a dictionary by its keys
This program orders dictionary entries by keys.
"""

def sort_by_keys(d):
    """Sort dictionary by keys"""
    sorted_dict = {}
    for key in sorted(d.keys()):
        sorted_dict[key] = d[key]
    return sorted_dict


# Main program
if __name__ == "__main__":
    test_dicts = [
        {'z': 26, 'a': 1, 'm': 13},
        {'name': 'John', 'age': 30, 'city': 'NYC'},
        {3: 'three', 1: 'one', 2: 'two'},
        {},
    ]
    
    print("Dictionary Key Sorter")
    print("-" * 40)
    for d in test_dicts:
        sorted_dict = sort_by_keys(d)
        print(f"Original: {d}")
        print(f"Sorted by keys: {sorted_dict}\n")

"""
OUTPUT:
Dictionary Key Sorter
----------------------------------------
Original: {'z': 26, 'a': 1, 'm': 13}
Sorted by keys: {'a': 1, 'm': 13, 'z': 26}

Original: {'name': 'John', 'age': 30, 'city': 'NYC'}
Sorted by keys: {'age': 30, 'city': 'NYC', 'name': 'John'}

Original: {3: 'three', 1: 'one', 2: 'two'}
Sorted by keys: {1: 'one', 2: 'two', 3: 'three'}

Original: {}
Sorted by keys: {}
"""
