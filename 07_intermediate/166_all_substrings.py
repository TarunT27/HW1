"""
Program 166: Find all substrings of a string
This program generates all possible substrings of a given string.
"""

def all_substrings(s):
    """Find all substrings"""
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return sorted(list(substrings))


# Main program
if __name__ == "__main__":
    test_cases = [
        "abc",
        "ab",
    ]
    
    print("All Substrings Finder")
    print("-" * 40)
    for s in test_cases:
        substrings = all_substrings(s)
        print(f"String: {s}")
        print(f"Substrings: {substrings}")
        print(f"Count: {len(substrings)}\n")

"""
OUTPUT:
All Substrings Finder
----------------------------------------
String: abc
Substrings: ['a', 'ab', 'abc', 'b', 'bc', 'c']
Count: 6

String: ab
Substrings: ['a', 'ab', 'b']
Count: 3
"""
