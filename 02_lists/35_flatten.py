"""
Program 35: Flatten a nested list
This program converts a nested list into a single-level list.
"""

def flatten_list(lst):
    """Flatten a nested list"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


# Main program
if __name__ == "__main__":
    test_lists = [
        [[1, 2], [3, 4], [5, 6]],
        [1, [2, 3], 4],
        [[[1, 2], 3], 4],
        [1, 2, 3],
        []
    ]
    
    print("List Flattener")
    print("-" * 40)
    for lst in test_lists:
        flattened = flatten_list(lst)
        print(f"{lst}")
        print(f"  -> {flattened}\n")

"""
OUTPUT:
List Flattener
----------------------------------------
[[1, 2], [3, 4], [5, 6]]
  -> [1, 2, 3, 4, 5, 6]

[1, [2, 3], 4]
  -> [1, 2, 3, 4]

[[[1, 2], 3], 4]
  -> [1, 2, 3, 4]

[1, 2, 3]
  -> [1, 2, 3]

[]
  -> []
"""
