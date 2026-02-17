"""
Program 125: Remove duplicate characters from a string (keeping order)
This program removes duplicates while preserving first occurrence.
"""

def remove_duplicate_chars(s):
    """Remove duplicate characters keeping order"""
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    return result


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "aabbcc", "abcabc", "mississippi"]
    
    print("Duplicate Character Remover")
    print("-" * 40)
    for s in test_strings:
        result = remove_duplicate_chars(s)
        print(f"'{s}' -> '{result}'")

"""
OUTPUT:
Duplicate Character Remover
----------------------------------------
'hello' -> 'helo'
'aabbcc' -> 'abc'
'abcabc' -> 'abc'
'mississippi' -> 'misp'
"""
