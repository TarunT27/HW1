"""
Program 22: Reverse a list without using built-in functions
This program reverses a list manually.
"""

def reverse_list(lst):
    """Reverse a list without using built-in functions"""
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list


def reverse_list_inplace(lst):
    """Reverse a list in place"""
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        ['a', 'b', 'c'],
        [1],
        []
    ]
    
    print("List Reverser (without built-in)")
    print("-" * 40)
    for lst in test_lists:
        reversed_lst = reverse_list(lst)
        print(f"{lst} -> {reversed_lst}")

"""
OUTPUT:
List Reverser (without built-in)
----------------------------------------
[1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
[10, 20, 30] -> [30, 20, 10]
['a', 'b', 'c'] -> ['c', 'b', 'a']
[1] -> [1]
[] -> []
"""
