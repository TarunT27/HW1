"""
Program 152: Find duplicate elements in a list
This program identifies all elements that appear more than once in a list.
"""

def find_duplicates(lst):
    """Find all duplicate elements"""
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)


# Main program
if __name__ == "__main__":
    test_cases = [
        [1, 2, 2, 3, 3, 3],
        ['a', 'b', 'a', 'c'],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1],
    ]
    
    print("Duplicate Elements Finder")
    print("-" * 40)
    for lst in test_cases:
        duplicates = find_duplicates(lst)
        print(f"List: {lst}")
        print(f"Duplicates: {duplicates}\n")

"""
OUTPUT:
Duplicate Elements Finder
----------------------------------------
List: [1, 2, 2, 3, 3, 3]
Duplicates: [2, 3]

List: ['a', 'b', 'a', 'c']
Duplicates: ['a']

List: [1, 2, 3, 4, 5]
Duplicates: []

List: [1, 1, 1, 1]
Duplicates: [1]
"""
