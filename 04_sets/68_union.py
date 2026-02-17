"""
Program 68: Find the union of two sets
This program combines all unique elements from both sets.
"""

def set_union(s1, s2):
    """Find union of two sets"""
    return s1 | s2


def set_union_manual(s1, s2):
    """Union without using | operator"""
    result = set()
    for item in s1:
        result.add(item)
    for item in s2:
        result.add(item)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ({1, 2, 3}, {3, 4, 5}),
        ({'a', 'b'}, {'b', 'c'}),
        ({1, 2}, set()),
        (set(), {1, 2}),
    ]
    
    print("Set Union Finder")
    print("-" * 40)
    for s1, s2 in test_cases:
        union = set_union(s1, s2)
        print(f"{s1} ∪ {s2} = {union}")

"""
OUTPUT:
Set Union Finder
----------------------------------------
{1, 2, 3} ∪ {3, 4, 5} = {1, 2, 3, 4, 5}
{'a', 'b'} ∪ {'b', 'c'} = {'a', 'b', 'c'}
{1, 2} ∪ set() = {1, 2}
set() ∪ {1, 2} = {1, 2}
"""
