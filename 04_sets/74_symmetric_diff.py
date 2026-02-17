"""
Program 74: Find the symmetric difference of two sets
This program finds elements in either set but not in both.
"""

def symmetric_difference(s1, s2):
    """Find symmetric difference"""
    return s1 ^ s2


def symmetric_difference_manual(s1, s2):
    """Symmetric difference without operator"""
    result = set()
    for item in s1:
        if item not in s2:
            result.add(item)
    for item in s2:
        if item not in s1:
            result.add(item)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ({1, 2, 3}, {3, 4, 5}),
        ({'a', 'b'}, {'b', 'c'}),
        ({1, 2}, {1, 2}),
        ({1, 2}, set()),
    ]
    
    print("Symmetric Difference Finder")
    print("-" * 40)
    for s1, s2 in test_cases:
        sym_diff = symmetric_difference(s1, s2)
        print(f"{s1} Δ {s2} = {sym_diff}")

"""
OUTPUT:
Symmetric Difference Finder
----------------------------------------
{1, 2, 3} Δ {3, 4, 5} = {1, 2, 4, 5}
{'a', 'b'} Δ {'b', 'c'} = {'a', 'c'}
{1, 2} Δ {1, 2} = set()
{1, 2} Δ set() = {1, 2}
"""
