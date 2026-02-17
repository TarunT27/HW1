"""
Program 163: Find longest common prefix
This program finds the longest common prefix string among an array of strings.
"""

def longest_common_prefix(strings):
    """Find longest common prefix"""
    if not strings:
        return ""
    
    min_len = min(len(s) for s in strings)
    for i in range(min_len):
        char = strings[0][i]
        for s in strings[1:]:
            if s[i] != char:
                return strings[0][:i]
    
    return strings[0][:min_len]


# Main program
if __name__ == "__main__":
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["hello", "help", "hemisphere"],
    ]
    
    print("Longest Common Prefix Finder")
    print("-" * 40)
    for strings in test_cases:
        prefix = longest_common_prefix(strings)
        print(f"Strings: {strings}")
        print(f"LCP: '{prefix}'\n")

"""
OUTPUT:
Longest Common Prefix Finder
----------------------------------------
Strings: ['flower', 'flow', 'flight']
LCP: 'fl'

Strings: ['dog', 'racecar', 'car']
LCP: ''

Strings: ['hello', 'help', 'hemisphere']
LCP: 'he'
"""
