"""
Program 142: Find median of a list of numbers
This program calculates the median value of a numeric list.
"""

def find_median(lst):
    """Find median"""
    sorted_list = sorted(lst)
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2


# Main program
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [5, 1, 3, 2, 4],
    ]
    
    print("Median Finder")
    print("-" * 40)
    for lst in test_cases:
        median = find_median(lst)
        print(f"List: {lst}")
        print(f"Median: {median}\n")

"""
OUTPUT:
Median Finder
----------------------------------------
List: [1, 2, 3, 4, 5]
Median: 3

List: [1, 2, 3, 4]
Median: 2.5

List: [5, 1, 3, 2, 4]
Median: 3
"""
