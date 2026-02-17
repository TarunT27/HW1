"""
Program 28: Merge two sorted lists
This program combines two sorted lists into one sorted list.
"""

def merge_sorted_lists(lst1, lst2):
    """Merge two sorted lists"""
    merged = []
    i, j = 0, 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    
    # Add remaining elements
    while i < len(lst1):
        merged.append(lst1[i])
        i += 1
    
    while j < len(lst2):
        merged.append(lst2[j])
        j += 1
    
    return merged


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5], [2, 4, 6]),
        ([1, 2, 3], [4, 5, 6]),
        ([], [1, 2, 3]),
        ([10], [5, 15]),
        ([], [])
    ]
    
    print("Sorted List Merger")
    print("-" * 40)
    for lst1, lst2 in test_cases:
        merged = merge_sorted_lists(lst1, lst2)
        print(f"{lst1} + {lst2}")
        print(f"  -> {merged}\n")

"""
OUTPUT:
Sorted List Merger
----------------------------------------
[1, 3, 5] + [2, 4, 6]
  -> [1, 2, 3, 4, 5, 6]

[1, 2, 3] + [4, 5, 6]
  -> [1, 2, 3, 4, 5, 6]

[] + [1, 2, 3]
  -> [1, 2, 3]

[10] + [5, 15]
  -> [5, 10, 15]

[] + []
  -> []
"""
