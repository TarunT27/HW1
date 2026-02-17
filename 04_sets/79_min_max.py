"""
Program 79: Find the smallest and largest elements in a set
This program identifies min and max values in a set.
"""

def find_min_max_set(s):
    """Find smallest and largest elements in a set"""
    if not s:
        return None, None
    min_val = min(s)
    max_val = max(s)
    return min_val, max_val


# Main program
if __name__ == "__main__":
    test_sets = [
        {5, 2, 8, 1, 9},
        {10, 20, 30},
        {-5, 0, 5},
        {42},
        set(),
    ]
    
    print("Set Min/Max Finder")
    print("-" * 40)
    for s in test_sets:
        min_val, max_val = find_min_max_set(s)
        print(f"{s} -> Min: {min_val}, Max: {max_val}")

"""
OUTPUT:
Set Min/Max Finder
----------------------------------------
{5, 2, 8, 1, 9} -> Min: 1, Max: 9
{10, 20, 30} -> Min: 10, Max: 30
{-5, 0, 5} -> Min: -5, Max: 5
{42} -> Min: 42, Max: 42
set() -> Min: None, Max: None
"""
