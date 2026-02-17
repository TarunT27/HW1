"""
Program 75: Check if two sets have any common elements
This program checks if sets share any elements.
"""

def have_common_elements(s1, s2):
    """Check if sets have common elements"""
    for item in s1:
        if item in s2:
            return True
    return False


# Main program
if __name__ == "__main__":
    test_cases = [
        ({1, 2, 3}, {3, 4, 5}),
        ({1, 2}, {3, 4, 5}),
        ({'a', 'b'}, {'a', 'c'}),
        (set(), {1, 2}),
        ({1}, {1}),
    ]
    
    print("Common Elements Checker")
    print("-" * 40)
    for s1, s2 in test_cases:
        has_common = have_common_elements(s1, s2)
        print(f"{s1} & {s2} have common -> {has_common}")

"""
OUTPUT:
Common Elements Checker
----------------------------------------
{1, 2, 3} & {3, 4, 5} have common -> True
{1, 2} & {3, 4, 5} have common -> False
{'a', 'b'} & {'a', 'c'} have common -> True
set() & {1, 2} have common -> False
{1} & {1} have common -> True
"""
