"""
Program 167: Check if string is subsequence of another
This program determines if one string is a subsequence of another string.
"""

def is_subsequence(s1, s2):
    """Check if s1 is subsequence of s2"""
    i = 0
    for char in s2:
        if i < len(s1) and char == s1[i]:
            i += 1
    return i == len(s1)


# Main program
if __name__ == "__main__":
    test_cases = [
        ("ace", "abcde"),
        ("aec", "abcde"),
        ("abc", "abc"),
    ]
    
    print("Subsequence Checker")
    print("-" * 40)
    for s1, s2 in test_cases:
        result = is_subsequence(s1, s2)
        print(f"Is '{s1}' subsequence of '{s2}'? {result}\n")

"""
OUTPUT:
Subsequence Checker
----------------------------------------
Is 'ace' subsequence of 'abcde'? True

Is 'aec' subsequence of 'abcde'? False

Is 'abc' subsequence of 'abc'? True
"""
