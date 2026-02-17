"""
Program 50: Merge two dictionaries
This program combines two dictionaries into one.
"""

def merge_dictionaries(d1, d2):
    """Merge two dictionaries"""
    merged = {}
    for key in d1:
        merged[key] = d1[key]
    for key in d2:
        merged[key] = d2[key]
    return merged


# Main program
if __name__ == "__main__":
    test_cases = [
        ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}),
        ({'x': 10}, {'x': 20, 'y': 30}),
        ({}, {'a': 1, 'b': 2}),
        ({'a': 1}, {}),
    ]
    
    print("Dictionary Merger")
    print("-" * 40)
    for d1, d2 in test_cases:
        merged = merge_dictionaries(d1, d2)
        print(f"{d1} + {d2}")
        print(f"  -> {merged}\n")

"""
OUTPUT:
Dictionary Merger
----------------------------------------
{'a': 1, 'b': 2} + {'c': 3, 'd': 4}
  -> {'a': 1, 'b': 2, 'c': 3, 'd': 4}

{'x': 10} + {'x': 20, 'y': 30}
  -> {'x': 20, 'y': 30}

{} + {'a': 1, 'b': 2}
  -> {'a': 1, 'b': 2}

{'a': 1} + {}
  -> {'a': 1}
"""
