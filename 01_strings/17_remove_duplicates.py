"""
Program 17: Remove duplicate characters from a string
This program removes all duplicate characters, keeping only first occurrence.
"""

def remove_duplicates(s):
    """Remove duplicate characters from a string"""
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    return result


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "programming", "aabbcc", "mississippi", "abcdef"]
    
    print("Duplicate Character Remover")
    print("-" * 40)
    for test in test_strings:
        result = remove_duplicates(test)
        print(f"'{test}' -> '{result}'")

"""
OUTPUT:
Duplicate Character Remover
----------------------------------------
'hello' -> 'helo'
'programming' -> 'progamin'
'aabbcc' -> 'abc'
'mississippi' -> 'misp'
'abcdef' -> 'abcdef'
"""
