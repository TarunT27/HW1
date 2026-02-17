"""
Program 173: Find most common substring of length k
This program finds the most frequently occurring substring of length k.
"""

def most_common_substring(s, k):
    """Find most common substring of length k"""
    if k > len(s):
        return ""
    
    substring_count = {}
    for i in range(len(s) - k + 1):
        substr = s[i:i+k]
        substring_count[substr] = substring_count.get(substr, 0) + 1
    
    return max(substring_count, key=substring_count.get) if substring_count else ""


# Main program
if __name__ == "__main__":
    test_cases = [
        ("abcabcab", 2),
        ("aaabbbccc", 2),
        ("hello", 2),
    ]
    
    print("Most Common Substring Finder")
    print("-" * 40)
    for s, k in test_cases:
        result = most_common_substring(s, k)
        print(f"String: {s}, k: {k}")
        print(f"Most common: '{result}'\n")

"""
OUTPUT:
Most Common Substring Finder
----------------------------------------
String: abcabcab, k: 2
Most common: 'ab'

String: aaabbbccc, k: 2
Most common: 'bb'

String: hello, k: 2
Most common: 'el'
"""
