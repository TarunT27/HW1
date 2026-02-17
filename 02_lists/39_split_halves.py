"""
Program 39: Split a list into two halves
This program divides a list into two equal parts.
"""

def split_in_halves(lst):
    """Split a list into two halves"""
    mid = len(lst) // 2
    return lst[:mid], lst[mid:]


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        []
    ]
    
    print("List Half Splitter")
    print("-" * 40)
    for lst in test_lists:
        first, second = split_in_halves(lst)
        print(f"{lst}")
        print(f"  -> First: {first}, Second: {second}\n")

"""
OUTPUT:
List Half Splitter
----------------------------------------
[1, 2, 3, 4, 5, 6]
  -> First: [1, 2, 3], Second: [4, 5, 6]

[1, 2, 3, 4, 5]
  -> First: [1, 2], Second: [3, 4, 5]

[1, 2]
  -> First: [1], Second: [2]

[1]
  -> First: [], Second: [1]

[]
  -> First: [], Second: []
"""
