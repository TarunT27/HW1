"""
Program 143: Count unique elements in a list
This program counts the number of unique (distinct) elements in a list.
"""

def count_unique(lst):
    """Count unique elements"""
    return len(set(lst))


# Main program
if __name__ == "__main__":
    test_cases = [
        [1, 2, 2, 3, 3, 3],
        ['a', 'b', 'a', 'c'],
        [1, 1, 1, 1],
        [],
    ]
    
    print("Unique Elements Counter")
    print("-" * 40)
    for lst in test_cases:
        count = count_unique(lst)
        print(f"List: {lst}")
        print(f"Unique count: {count}")
        print(f"Unique elements: {set(lst)}\n")

"""
OUTPUT:
Unique Elements Counter
----------------------------------------
List: [1, 2, 2, 3, 3, 3]
Unique count: 3
Unique elements: {1, 2, 3}

List: ['a', 'b', 'a', 'c']
Unique count: 3
Unique elements: {'a', 'b', 'c'}

List: [1, 1, 1, 1]
Unique count: 1
Unique elements: {1}

List: []
Unique count: 0
Unique elements: set()
"""
