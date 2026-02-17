"""
Program 77: Check if a set is disjoint from another set
This program checks if two sets have no common elements.
"""

def is_disjoint(s1, s2):
    """Check if sets are disjoint"""
    for item in s1:
        if item in s2:
            return False
    return True


# Main program
if __name__ == "__main__":
    test_cases = [
        ({1, 2, 3}, {4, 5, 6}),
        ({1, 2}, {2, 3}),
        ({'a', 'b'}, {'c', 'd'}),
        (set(), {1, 2}),
        ({1}, {1}),
    ]
    
    print("Disjoint Checker")
    print("-" * 40)
    for s1, s2 in test_cases:
        result = is_disjoint(s1, s2)
        print(f"{s1} disjoint {s2} -> {result}")

"""
OUTPUT:
Disjoint Checker
----------------------------------------
{1, 2, 3} disjoint {4, 5, 6} -> True
{1, 2} disjoint {2, 3} -> False
{'a', 'b'} disjoint {'c', 'd'} -> True
set() disjoint {1, 2} -> True
{1} disjoint {1} -> False
"""
