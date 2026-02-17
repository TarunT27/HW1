"""
Program 71: Find the difference between two sets
This program finds elements in first set but not in second.
"""

def set_difference(s1, s2):
    """Find difference of two sets"""
    return s1 - s2


def set_difference_manual(s1, s2):
    """Difference without using - operator"""
    result = set()
    for item in s1:
        if item not in s2:
            result.add(item)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ({1, 2, 3, 4}, {3, 4, 5, 6}),
        ({'a', 'b', 'c'}, {'b', 'c', 'd'}),
        ({1, 2, 3}, {1, 2, 3}),
        ({1, 2}, set()),
    ]
    
    print("Set Difference Finder")
    print("-" * 40)
    for s1, s2 in test_cases:
        diff = set_difference(s1, s2)
        print(f"{s1} - {s2} = {diff}")

"""
OUTPUT:
Set Difference Finder
----------------------------------------
{1, 2, 3, 4} - {3, 4, 5, 6} = {1, 2}
{'a', 'b', 'c'} - {'b', 'c', 'd'} = {'a'}
{1, 2, 3} - {1, 2, 3} = set()
{1, 2} - set() = {1, 2}
"""
