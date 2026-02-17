"""
Program 124: Find all substrings of a given string
This program generates all substrings.
"""

def all_substrings(s):
    """Find all substrings of a string"""
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return sorted(substrings)


# Main program
if __name__ == "__main__":
    test_strings = ["abc", "ab", "a"]
    
    print("All Substrings Finder")
    print("-" * 40)
    for s in test_strings:
        subs = all_substrings(s)
        print(f"'{s}' -> {subs}\n")

"""
OUTPUT:
All Substrings Finder
----------------------------------------
'abc' -> ['a', 'ab', 'abc', 'b', 'bc', 'c']

'ab' -> ['a', 'ab', 'b']

'a' -> ['a']
"""
