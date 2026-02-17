"""
Program 80: Find the length of a set without using len() function
This program manually calculates set size.
"""

def set_length(s):
    """Find length of set without len()"""
    count = 0
    for _ in s:
        count += 1
    return count


# Main program
if __name__ == "__main__":
    test_sets = [
        {1, 2, 3, 4, 5},
        {'a', 'b', 'c'},
        {1},
        set(),
    ]
    
    print("Set Length Finder (without len())")
    print("-" * 40)
    for s in test_sets:
        length = set_length(s)
        actual_len = len(s)
        print(f"{s} -> {length} (actual: {actual_len})")

"""
OUTPUT:
Set Length Finder (without len())
----------------------------------------
{1, 2, 3, 4, 5} -> 5 (actual: 5)
{'a', 'b', 'c'} -> 3 (actual: 3)
{1} -> 1 (actual: 1)
set() -> 0 (actual: 0)
"""
