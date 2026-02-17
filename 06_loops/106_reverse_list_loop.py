"""
Program 106: Reverse a list using a loop
This program reverses list elements.
"""

def reverse_list_loop(lst):
    """Reverse list using loop"""
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c'],
        [1],
        []
    ]
    
    print("List Reverser (using loop)")
    print("-" * 40)
    for lst in test_lists:
        reversed_lst = reverse_list_loop(lst)
        print(f"{lst} -> {reversed_lst}")

"""
OUTPUT:
List Reverser (using loop)
----------------------------------------
[1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
['a', 'b', 'c'] -> ['c', 'b', 'a']
[1] -> [1]
[] -> []
"""
