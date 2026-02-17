"""
Program 12: Find the index of the first occurrence of a substring
This program finds where a substring first appears in a string.
"""

def find_first_occurrence(s, substring):
    """Find the index of first occurrence of substring"""
    # Using built-in find()
    return s.find(substring)


def find_first_occurrence_manual(s, substring):
    """Find first occurrence manually"""
    for i in range(len(s) - len(substring) + 1):
        if s[i:i+len(substring)] == substring:
            return i
    return -1  # Not found


# Main program
if __name__ == "__main__":
    test_cases = [
        ("hello world", "world"),
        ("python programming", "p"),
        ("mississippi", "ss"),
        ("hello", "xyz"),
        ("aaa", "aa")
    ]
    
    print("Substring Index Finder")
    print("-" * 40)
    for string, substring in test_cases:
        index = find_first_occurrence(string, substring)
        print(f"'{substring}' in '{string}' -> Index: {index}")

"""
OUTPUT:
Substring Index Finder
----------------------------------------
'world' in 'hello world' -> Index: 6
'p' in 'python programming' -> Index: 0
'ss' in 'mississippi' -> Index: 2
'xyz' in 'hello' -> Index: -1
'aa' in 'aaa' -> Index: 0
"""
