"""
Program 127: Find the longest palindromic substring in a given string
This program identifies longest palindrome substring.
"""

def longest_palindromic_substring(s):
    """Find longest palindromic substring"""
    if not s:
        return ""
    
    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                if len(substring) > len(longest):
                    longest = substring
    return longest


# Main program
if __name__ == "__main__":
    test_strings = ["babad", "cbbd", "a", "ac", "racecar"]
    
    print("Longest Palindromic Substring Finder")
    print("-" * 40)
    for s in test_strings:
        result = longest_palindromic_substring(s)
        print(f"'{s}' -> '{result}'")

"""
OUTPUT:
Longest Palindromic Substring Finder
----------------------------------------
'babad' -> 'bab'
'cbbd' -> 'bb'
'a' -> 'a'
'ac' -> 'a'
'racecar' -> 'racecar'
"""
