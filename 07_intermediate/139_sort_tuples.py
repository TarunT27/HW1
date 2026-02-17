"""
Program 139: Sort list of tuples by second element
This program sorts a list of tuples based on the second element.
"""

def sort_tuples_by_second(lst):
    """Sort tuples by second element"""
    return sorted(lst, key=lambda x: x[1])


# Main program
if __name__ == "__main__":
    test_cases = [
        [(3, 'c'), (1, 'a'), (2, 'b')],
        [(5, 10), (3, 30), (8, 20)],
    ]
    
    print("Sort Tuples by Second Element")
    print("-" * 40)
    for lst in test_cases:
        result = sort_tuples_by_second(lst)
        print(f"Original: {lst}")
        print(f"Sorted: {result}\n")

"""
OUTPUT:
Sort Tuples by Second Element
----------------------------------------
Original: [(3, 'c'), (1, 'a'), (2, 'b')]
Sorted: [(1, 'a'), (2, 'b'), (3, 'c')]

Original: [(5, 10), (3, 30), (8, 20)]
Sorted: [(5, 10), (8, 20), (3, 30)]
"""
