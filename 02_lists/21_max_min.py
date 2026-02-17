"""
Program 21: Find the maximum and minimum elements in a list
This program identifies the largest and smallest values.
"""

def find_max_min(lst):
    """Find maximum and minimum in a list"""
    max_val = lst[0]
    min_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val


# Main program
if __name__ == "__main__":
    test_lists = [
        [5, 2, 8, 1, 9],
        [10, 20, 30],
        [-5, -2, -10],
        [0],
        [3, 3, 3, 3]
    ]
    
    print("Max and Min Finder")
    print("-" * 40)
    for lst in test_lists:
        max_val, min_val = find_max_min(lst)
        print(f"{lst}")
        print(f"  Max: {max_val}, Min: {min_val}\n")

"""
OUTPUT:
Max and Min Finder
----------------------------------------
[5, 2, 8, 1, 9]
  Max: 9, Min: 1

[10, 20, 30]
  Max: 30, Min: 10

[-5, -2, -10]
  Max: -2, Min: -10

[0]
  Max: 0, Min: 0

[3, 3, 3, 3]
  Max: 3, Min: 3
"""
