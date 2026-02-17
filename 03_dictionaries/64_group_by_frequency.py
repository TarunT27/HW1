"""
Program 64: Group elements in a list by frequency using a dictionary
This program groups elements based on how often they appear.
"""

def group_by_frequency(lst):
    """Group elements by their frequency"""
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    # Group by frequency
    groups = {}
    for item, count in freq.items():
        if count not in groups:
            groups[count] = []
        groups[count].append(item)
    
    return groups


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 1, 2, 2, 2, 3, 3, 3, 3],
        ['a', 'a', 'b', 'c', 'c', 'c'],
        [1, 2, 3, 4, 5],
        [5, 5, 5, 5],
        []
    ]
    
    print("Element Grouper by Frequency")
    print("-" * 40)
    for lst in test_lists:
        groups = group_by_frequency(lst)
        print(f"{lst}")
        print(f"  -> {groups}\n")

"""
OUTPUT:
Element Grouper by Frequency
----------------------------------------
[1, 1, 2, 2, 2, 3, 3, 3, 3]
  -> {2: [1], 3: [2], 4: [3]}

['a', 'a', 'b', 'c', 'c', 'c']
  -> {2: ['a'], 1: ['b'], 3: ['c']}

[1, 2, 3, 4, 5]
  -> {1: [1, 2, 3, 4, 5]}

[5, 5, 5, 5]
  -> {4: [5]}

[]
  -> {}
"""
