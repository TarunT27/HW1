"""
Program 149: Find key with maximum value in dictionary
This program identifies which key has the maximum value in a dictionary.
"""

def max_key_value(d):
    """Find key with maximum value"""
    if not d:
        return None
    return max(d, key=d.get)


# Main program
if __name__ == "__main__":
    test_cases = [
        {'apple': 5, 'banana': 10, 'orange': 3},
        {'a': 1, 'b': 2, 'c': 2},
        {'x': 100},
    ]
    
    print("Find Key with Maximum Value")
    print("-" * 40)
    for d in test_cases:
        key = max_key_value(d)
        value = d[key]
        print(f"Dictionary: {d}")
        print(f"Max key: {key}, Value: {value}\n")

"""
OUTPUT:
Find Key with Maximum Value
----------------------------------------
Dictionary: {'apple': 5, 'banana': 10, 'orange': 3}
Max key: banana, Value: 10

Dictionary: {'a': 1, 'b': 2, 'c': 2}
Max key: b, Value: 2

Dictionary: {'x': 100}
Max key: x, Value: 100
"""
