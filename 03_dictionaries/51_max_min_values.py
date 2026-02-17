"""
Program 51: Find the maximum and minimum value in a dictionary
This program identifies largest and smallest values.
"""

def find_max_min_values(d):
    """Find max and min values in dictionary"""
    if not d:
        return None, None
    
    max_val = max(d.values())
    min_val = min(d.values())
    return max_val, min_val


# Main program
if __name__ == "__main__":
    test_cases = [
        {'a': 5, 'b': 2, 'c': 8, 'd': 1},
        {'x': 10, 'y': 10, 'z': 10},
        {'name': 'John'},
        {'scores': 95, 'grade': 87},
    ]
    
    print("Dictionary Max/Min Value Finder")
    print("-" * 40)
    for d in test_cases:
        max_val, min_val = find_max_min_values(d)
        print(f"{d}")
        print(f"  Max: {max_val}, Min: {min_val}\n")

"""
OUTPUT:
Dictionary Max/Min Value Finder
----------------------------------------
{'a': 5, 'b': 2, 'c': 8, 'd': 1}
  Max: 8, Min: 1

{'x': 10, 'y': 10, 'z': 10}
  Max: 10, Min: 10

{'name': 'John'}
  Max: None, Min: None

{'scores': 95, 'grade': 87}
  Max: 95, Min: 87
"""
