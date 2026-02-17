"""
Program 145: Find most frequent element in list
This program identifies the element that appears most frequently in a list.
"""

def most_frequent(lst):
    """Find most frequent element"""
    if not lst:
        return None
    
    freq_dict = {}
    for item in lst:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    
    return max(freq_dict, key=freq_dict.get)


# Main program
if __name__ == "__main__":
    test_cases = [
        [1, 2, 2, 3, 3, 3],
        ['a', 'b', 'a', 'a', 'c'],
        [5, 5, 5, 5],
    ]
    
    print("Most Frequent Element Finder")
    print("-" * 40)
    for lst in test_cases:
        result = most_frequent(lst)
        freq_dict = {}
        for item in lst:
            freq_dict[item] = freq_dict.get(item, 0) + 1
        print(f"List: {lst}")
        print(f"Frequencies: {freq_dict}")
        print(f"Most frequent: {result}\n")

"""
OUTPUT:
Most Frequent Element Finder
----------------------------------------
List: [1, 2, 2, 3, 3, 3]
Frequencies: {1: 1, 2: 2, 3: 3}
Most frequent: 3

List: ['a', 'b', 'a', 'a', 'c']
Frequencies: {'a': 3, 'b': 1, 'c': 1}
Most frequent: a

List: [5, 5, 5, 5]
Frequencies: {5: 4}
Most frequent: 5
"""
