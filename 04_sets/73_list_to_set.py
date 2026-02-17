"""
Program 73: Convert a list into a set and remove duplicates
This program uses sets to eliminate duplicate values.
"""

def list_to_set(lst):
    """Convert list to set removing duplicates"""
    return set(lst)


def list_to_set_manual(lst):
    """Convert to set manually"""
    s = set()
    for item in lst:
        s.add(item)
    return s


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 2, 3, 3, 3, 4],
        ['a', 'a', 'b', 'c', 'c'],
        [1, 2, 3, 4, 5],
        [],
        [1, 1, 1, 1]
    ]
    
    print("List to Set Converter (Remove Duplicates)")
    print("-" * 40)
    for lst in test_lists:
        s = list_to_set(lst)
        print(f"{lst}")
        print(f"  -> {s}\n")

"""
OUTPUT:
List to Set Converter (Remove Duplicates)
----------------------------------------
[1, 2, 2, 3, 3, 3, 4]
  -> {1, 2, 3, 4}

['a', 'a', 'b', 'c', 'c']
  -> {'a', 'b', 'c'}

[1, 2, 3, 4, 5]
  -> {1, 2, 3, 4, 5}

[]
  -> set()

[1, 1, 1, 1]
  -> {1}
"""
