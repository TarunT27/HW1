"""
Program 137: Flatten a list of lists into a single list
This program flattens nested lists.
"""

def flatten_nested(lst):
    """Flatten nested list"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_nested(item))
        else:
            result.append(item)
    return result


# Main program
if __name__ == "__main__":
    test_lists = [[[1, 2], [3, 4]], [1, [2, 3], 4]]
    
    print("Nested List Flattener")
    print("-" * 40)
    for lst in test_lists:
        result = flatten_nested(lst)
        print(f"{lst} -> {result}")

"""
OUTPUT:
Nested List Flattener
----------------------------------------
[[1, 2], [3, 4]] -> [1, 2, 3, 4]
[1, [2, 3], 4] -> [1, 2, 3, 4]
"""
