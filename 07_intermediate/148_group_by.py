"""
Program 148: Group list elements by dictionary key
This program groups elements based on a key function and returns as dictionary.
"""

def group_by_key(lst, key_func):
    """Group elements by key"""
    result = {}
    for item in lst:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


# Main program
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Group Elements by Key")
    print("-" * 40)
    print(f"Numbers: {numbers}\n")
    
    # Group by even/odd
    grouped = group_by_key(numbers, lambda x: 'even' if x % 2 == 0 else 'odd')
    print("Grouped by even/odd:")
    for key, items in grouped.items():
        print(f"  {key}: {items}\n")
    
    # Group by divisibility by 3
    grouped = group_by_key(numbers, lambda x: 'divisible by 3' if x % 3 == 0 else 'not divisible by 3')
    print("Grouped by divisibility by 3:")
    for key, items in grouped.items():
        print(f"  {key}: {items}")

"""
OUTPUT:
Group Elements by Key
----------------------------------------
Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Grouped by even/odd:
  even: [2, 4, 6, 8, 10]

  odd: [1, 3, 5, 7, 9]


Grouped by divisibility by 3:
  not divisible by 3: [1, 2, 4, 5, 7, 8, 10]

  divisible by 3: [3, 6, 9]
"""
