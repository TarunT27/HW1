"""
Program 147: Count frequency of elements using dictionary
This program creates a frequency dictionary from a list of elements.
"""

def frequency_dict(lst):
    """Create frequency dictionary"""
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq


# Main program
if __name__ == "__main__":
    test_cases = [
        [1, 2, 2, 3, 3, 3],
        ['a', 'b', 'a', 'c'],
        [1, 1, 1, 1],
    ]
    
    print("Frequency Dictionary Creator")
    print("-" * 40)
    for lst in test_cases:
        freq = frequency_dict(lst)
        print(f"List: {lst}")
        print(f"Frequency: {freq}\n")

"""
OUTPUT:
Frequency Dictionary Creator
----------------------------------------
List: [1, 2, 2, 3, 3, 3]
Frequency: {1: 1, 2: 2, 3: 3}

List: ['a', 'b', 'a', 'c']
Frequency: {'a': 2, 'b': 1, 'c': 1}

List: [1, 1, 1, 1]
Frequency: {1: 4}
"""
