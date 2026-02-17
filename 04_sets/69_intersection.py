"""
Program 69: Find the intersection of two sets
This program finds common elements in both sets.
"""

def set_intersection(s1, s2):
    """Find intersection of two sets"""
    return s1 & s2


def set_intersection_manual(s1, s2):
    """Intersection without using & operator"""
    result = set()
    for item in s1:
        if item in s2:
            result.add(item)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ({1, 2, 3, 4}, {3, 4, 5, 6}),
        ({'a', 'b', 'c'}, {'b', 'c', 'd'}),
        ({1, 2, 3}, {4, 5, 6}),
        ({1, 2}, {1, 2}),
    ]
    
    print("Set Intersection Finder")
    print("-" * 40)
    for s1, s2 in test_cases:
        intersection = set_intersection(s1, s2)
        print(f"{s1} ∩ {s2} = {intersection}")

"""
OUTPUT:
Set Intersection Finder
----------------------------------------
{1, 2, 3, 4} ∩ {3, 4, 5, 6} = {3, 4}
{'a', 'b', 'c'} ∩ {'b', 'c', 'd'} = {'b', 'c'}
{1, 2, 3} ∩ {4, 5, 6} = set()
{1, 2} ∩ {1, 2} = {1, 2}
"""
