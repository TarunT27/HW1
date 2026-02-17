"""
Program 24: Remove duplicates from a list
This program removes all duplicate elements from a list.
"""

def remove_duplicates(lst):
    """Remove duplicates from a list"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def remove_duplicates_list_comp(lst):
    """Remove duplicates using list comprehension with seen set"""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 2, 3, 4, 4, 5],
        [5, 5, 5, 5],
        [1, 2, 3, 4, 5],
        ['a', 'b', 'a', 'c'],
        []
    ]
    
    print("Duplicate Remover")
    print("-" * 40)
    for lst in test_lists:
        result = remove_duplicates(lst)
        print(f"{lst} -> {result}")

"""
OUTPUT:
Duplicate Remover
----------------------------------------
[1, 2, 2, 3, 4, 4, 5] -> [1, 2, 3, 4, 5]
[5, 5, 5, 5] -> [5]
[1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
['a', 'b', 'a', 'c'] -> ['a', 'b', 'c']
[] -> []
"""
