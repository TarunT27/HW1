"""
Program 155: Find common characters between strings
This program identifies characters that appear in all provided strings.
"""

def common_characters(*strings):
    """Find common characters"""
    if not strings:
        return []
    
    common = set(strings[0])
    for s in strings[1:]:
        common &= set(s)
    return sorted(list(common))


# Main program
if __name__ == "__main__":
    test_cases = [
        ("hello", "world"),
        ("abc", "bcd", "cde"),
        ("python", "java"),
    ]
    
    print("Common Characters Finder")
    print("-" * 40)
    for strings in test_cases:
        common = common_characters(*strings)
        print(f"Strings: {strings}")
        print(f"Common chars: {common}\n")

"""
OUTPUT:
Common Characters Finder
----------------------------------------
Strings: ('hello', 'world')
Common chars: ['l', 'o']

Strings: ('abc', 'bcd', 'cde')
Common chars: ['c']

Strings: ('python', 'java')
Common chars: ['a']
"""
