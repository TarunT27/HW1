"""
Program 132: Find the cumulative sum of elements in a list
This program calculates running total.
"""

def cumulative_sum_list(lst):
    """Calculate cumulative sum"""
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result


# Main program
if __name__ == "__main__":
    test_lists = [[1, 2, 3, 4], [10, 20, 30], [5]]
    
    print("Cumulative Sum Calculator")
    print("-" * 40)
    for lst in test_lists:
        result = cumulative_sum_list(lst)
        print(f"{lst} -> {result}")

"""
OUTPUT:
Cumulative Sum Calculator
----------------------------------------
[1, 2, 3, 4] -> [1, 3, 6, 10]
[10, 20, 30] -> [10, 30, 60]
[5] -> [5]
"""
