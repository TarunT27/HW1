"""
Program 70: Check if a set is a subset of another set
This program checks if all elements of one set are in another.
"""

def is_subset(s1, s2):
    """Check if s1 is subset of s2"""
    for item in s1:
        if item not in s2:
            return False
    return True


# Main program
if __name__ == "__main__":
    test_cases = [
        ({1, 2}, {1, 2, 3, 4}),
        ({1, 2, 3}, {1, 2}),
        ({1, 2, 3}, {1, 2, 3}),
        (set(), {1, 2}),
        ({1}, set()),
    ]
    
    print("Subset Checker")
    print("-" * 40)
    for s1, s2 in test_cases:
        result = is_subset(s1, s2)
        print(f"{s1} ⊆ {s2} -> {result}")

"""
OUTPUT:
Subset Checker
----------------------------------------
{1, 2} ⊆ {1, 2, 3, 4} -> True
{1, 2, 3} ⊆ {1, 2} -> False
{1, 2, 3} ⊆ {1, 2, 3} -> True
set() ⊆ {1, 2} -> True
{1} ⊆ set() -> False
"""
