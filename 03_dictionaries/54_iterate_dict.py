"""
Program 54: Iterate over dictionary keys and values
This program demonstrates dictionary iteration.
"""

def iterate_dict(d):
    """Iterate over dictionary keys and values"""
    for key in d:
        print(f"Key: {key}, Value: {d[key]}")


# Main program
if __name__ == "__main__":
    test_dicts = [
        {'name': 'John', 'age': 30, 'city': 'NYC'},
        {'a': 1, 'b': 2, 'c': 3},
        {},
    ]
    
    print("Dictionary Iterator")
    print("-" * 40)
    for d in test_dicts:
        print(f"Dictionary: {d}")
        iterate_dict(d)
        print()

"""
OUTPUT:
Dictionary Iterator
----------------------------------------
Dictionary: {'name': 'John', 'age': 30, 'city': 'NYC'}
Key: name, Value: John
Key: age, Value: 30
Key: city, Value: NYC

Dictionary: {'a': 1, 'b': 2, 'c': 3}
Key: a, Value: 1
Key: b, Value: 2
Key: c, Value: 3

Dictionary: {}
"""
