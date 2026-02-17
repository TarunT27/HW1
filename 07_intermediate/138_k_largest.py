"""
Program 138: Find k largest elements in a list
This program returns the k largest elements from a list.
"""

import heapq

def k_largest(lst, k):
    """Find k largest elements"""
    return heapq.nlargest(k, lst)


# Main program
if __name__ == "__main__":
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6], 3),
        ([10, 20, 30, 40, 50], 2),
        ([1, 2, 3, 4, 5], 5),
    ]
    
    print("K Largest Elements Finder")
    print("-" * 40)
    for lst, k in test_cases:
        result = k_largest(lst, k)
        print(f"List: {lst}, k={k}")
        print(f"Result: {result}\n")

"""
OUTPUT:
K Largest Elements Finder
----------------------------------------
List: [3, 1, 4, 1, 5, 9, 2, 6], k=3
Result: [9, 6, 5]

List: [10, 20, 30, 40, 50], k=2
Result: [50, 40]

List: [1, 2, 3, 4, 5], k=5
Result: [5, 4, 3, 2, 1]
"""
