"""
Program 129: Remove all characters except alphabets from a string
This program filters non-alphabetic characters.
"""

def remove_non_alphabetic(s):
    """Remove all non-alphabetic characters"""
    result = ""
    for char in s:
        if char.isalpha():
            result += char
    return result


# Main program
if __name__ == "__main__":
    test_strings = ["hello123", "abc!@#def", "12345", "abc"]
    
    print("Non-Alphabetic Character Remover")
    print("-" * 40)
    for s in test_strings:
        result = remove_non_alphabetic(s)
        print(f"'{s}' -> '{result}'")

"""
OUTPUT:
Non-Alphabetic Character Remover
----------------------------------------
'hello123' -> 'hello'
'abc!@#def' -> 'abcdef'
'12345' -> ''
'abc' -> 'abc'
"""
