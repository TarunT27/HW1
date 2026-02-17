"""
Program 157: Remove all instances of a character
This program removes all occurrences of a specific character from a string.
"""

def remove_char(s, char):
    """Remove all instances of character"""
    return s.replace(char, '')


# Main program
if __name__ == "__main__":
    test_cases = [
        ("hello", "l"),
        ("programming", "g"),
        ("aabbcc", "b"),
    ]
    
    print("Remove Character from String")
    print("-" * 40)
    for s, char in test_cases:
        result = remove_char(s, char)
        print(f"String: {s}, Char: '{char}'")
        print(f"Result: {result}\n")

"""
OUTPUT:
Remove Character from String
----------------------------------------
String: hello, Char: 'l'
Result: heo

String: programming, Char: 'g'
Result: prorammin

String: aabbcc, Char: 'b'
Result: aacc
"""
