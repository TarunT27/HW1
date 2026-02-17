"""
Program 160: Find last occurrence index of element
This program finds the index of the last occurrence of an element in a list.
"""

def last_occurrence(lst, element):
    """Find last occurrence index"""
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == element:
            return i
    return -1


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 2, 4, 2], 2),
        (['a', 'b', 'a', 'c'], 'a'),
        ([1, 2, 3], 4),
    ]
    
    print("Last Occurrence Finder")
    print("-" * 40)
    for lst, element in test_cases:
        index = last_occurrence(lst, element)
        print(f"List: {lst}, Element: {element}")
        print(f"Last index: {index}\n")

"""
OUTPUT:
Last Occurrence Finder
----------------------------------------
List: [1, 2, 3, 2, 4, 2], Element: 2
Last index: 5

List: ['a', 'b', 'a', 'c'], Element: 'a'
Last index: 2

List: [1, 2, 3], Element: 4
Last index: -1
"""
