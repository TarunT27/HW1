"""
Program 40: Find the cumulative sum of elements in a list
This program calculates running total at each position.
"""

def cumulative_sum(lst):
    """Find cumulative sum of elements in a list"""
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [5],
        [1, -2, 3, -4],
        []
    ]
    
    print("Cumulative Sum Calculator")
    print("-" * 40)
    for lst in test_lists:
        cum_sum = cumulative_sum(lst)
        print(f"{lst}")
        print(f"  -> {cum_sum}\n")

"""
OUTPUT:
Cumulative Sum Calculator
----------------------------------------
[1, 2, 3, 4, 5]
  -> [1, 3, 6, 10, 15]

[10, 20, 30]
  -> [10, 30, 60]

[5]
  -> [5]

[1, -2, 3, -4]
  -> [1, -1, 2, -2]

[]
  -> []
"""
