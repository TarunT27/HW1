"""
Program 76: Check if a set is a superset of another set
This program checks if one set contains all elements of another.
"""

def is_superset(s1, s2):
    """Check if s1 is superset of s2"""
    for item in s2:
        if item not in s1:
            return False
    return True


# Main program
if __name__ == "__main__":
    test_cases = [
        ({1, 2, 3, 4}, {1, 2}),
        ({1, 2}, {1, 2, 3}),
        ({1, 2, 3}, {1, 2, 3}),
        ({1, 2}, set()),
        (set(), {1}),
    ]
    
    print("Superset Checker")
    print("-" * 40)
    for s1, s2 in test_cases:
        result = is_superset(s1, s2)
        print(f"{s1} ⊇ {s2} -> {result}")

"""
OUTPUT:
Superset Checker
----------------------------------------
{1, 2, 3, 4} ⊇ {1, 2} -> True
{1, 2} ⊇ {1, 2, 3} -> False
{1, 2, 3} ⊇ {1, 2, 3} -> True
{1, 2} ⊇ set() -> True
set() ⊇ {1} -> False
"""
