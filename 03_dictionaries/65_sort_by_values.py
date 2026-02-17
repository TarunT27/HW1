"""
Program 65: Sort a dictionary by its values
This program orders dictionary entries by their values.
"""

def sort_by_values(d):
    """Sort dictionary by values"""
    sorted_items = []
    for key, value in d.items():
        sorted_items.append((key, value))
    
    # Simple bubble sort by values
    for i in range(len(sorted_items)):
        for j in range(0, len(sorted_items) - i - 1):
            if sorted_items[j][1] > sorted_items[j + 1][1]:
                sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]
    
    sorted_dict = {}
    for key, value in sorted_items:
        sorted_dict[key] = value
    
    return sorted_dict


# Main program
if __name__ == "__main__":
    test_dicts = [
        {'z': 26, 'a': 1, 'm': 13},
        {'score1': 85, 'score2': 92, 'score3': 78},
        {'x': 10, 'y': 10, 'z': 10},
        {},
    ]
    
    print("Dictionary Value Sorter")
    print("-" * 40)
    for d in test_dicts:
        sorted_dict = sort_by_values(d)
        print(f"Original: {d}")
        print(f"Sorted by values: {sorted_dict}\n")

"""
OUTPUT:
Dictionary Value Sorter
----------------------------------------
Original: {'z': 26, 'a': 1, 'm': 13}
Sorted by values: {'a': 1, 'm': 13, 'z': 26}

Original: {'score1': 85, 'score2': 92, 'score3': 78}
Sorted by values: {'score3': 78, 'score1': 85, 'score2': 92}

Original: {'x': 10, 'y': 10, 'z': 10}
Sorted by values: {'x': 10, 'y': 10, 'z': 10}

Original: {}
Sorted by values: {}
"""
