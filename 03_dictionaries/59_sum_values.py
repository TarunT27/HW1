"""
Program 59: Calculate the sum of values in a dictionary
This program adds up all numeric values.
"""

def sum_of_values(d):
    """Calculate sum of all values in dictionary"""
    total = 0
    for value in d.values():
        if isinstance(value, (int, float)):
            total += value
    return total


# Main program
if __name__ == "__main__":
    test_dicts = [
        {'a': 10, 'b': 20, 'c': 30},
        {'x': 5, 'y': 15, 'z': 10},
        {'score1': 85, 'score2': 90, 'score3': 95},
        {},
        {'a': 100},
    ]
    
    print("Dictionary Values Sum Calculator")
    print("-" * 40)
    for d in test_dicts:
        total = sum_of_values(d)
        print(f"{d} -> Sum: {total}")

"""
OUTPUT:
Dictionary Values Sum Calculator
----------------------------------------
{'a': 10, 'b': 20, 'c': 30} -> Sum: 60
{'x': 5, 'y': 15, 'z': 10} -> Sum: 30
{'score1': 85, 'score2': 90, 'score3': 95} -> Sum: 270
{} -> Sum: 0
{'a': 100} -> Sum: 100
"""
