"""
Program 45: Multiply all elements in a list by a given number
This program scales all list elements by a factor.
"""

def multiply_all(lst, factor):
    """Multiply all elements by a factor"""
    result = []
    for num in lst:
        result.append(num * factor)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),
        ([10, 20, 30], 3),
        ([5], 10),
        ([1, -2, 3], 2),
        ([], 5)
    ]
    
    print("List Multiplier")
    print("-" * 40)
    for lst, factor in test_cases:
        result = multiply_all(lst, factor)
        print(f"{lst} * {factor} -> {result}")

"""
OUTPUT:
List Multiplier
----------------------------------------
[1, 2, 3, 4, 5] * 2 -> [2, 4, 6, 8, 10]
[10, 20, 30] * 3 -> [30, 60, 90]
[5] * 10 -> [50]
[1, -2, 3] * 2 -> [2, -4, 6]
[] * 5 -> []
"""
