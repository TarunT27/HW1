"""
Program 23: Sort a list of numbers
This program sorts numbers in ascending order.
"""

def bubble_sort(lst):
    """Sort using bubble sort algorithm"""
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Main program
if __name__ == "__main__":
    test_lists = [
        [5, 2, 8, 1, 9],
        [10, 20, 30],
        [3, 1, 4, 1, 5, 9],
        [0, -5, 10, -2],
        [42]
    ]
    
    print("List Sorter")
    print("-" * 40)
    for lst in test_lists:
        sorted_lst = bubble_sort(lst)
        print(f"{lst}")
        print(f"  -> {sorted_lst}\n")

"""
OUTPUT:
List Sorter
----------------------------------------
[5, 2, 8, 1, 9]
  -> [1, 2, 5, 8, 9]

[10, 20, 30]
  -> [10, 20, 30]

[3, 1, 4, 1, 5, 9]
  -> [1, 1, 3, 4, 5, 9]

[0, -5, 10, -2]
  -> [-5, -2, 0, 10]

[42]
  -> [42]
"""
