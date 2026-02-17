"""
Program 20: Convert a string to a list of characters
This program breaks a string into individual character elements.
"""

def string_to_char_list(s):
    """Convert string to a list of characters"""
    return list(s)


def string_to_char_list_manual(s):
    """Convert string to list manually"""
    char_list = []
    for char in s:
        char_list.append(char)
    return char_list


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "python", "123abc", ""]
    
    print("String to Character List Converter")
    print("-" * 40)
    for test in test_strings:
        char_list = string_to_char_list(test)
        print(f"'{test}' -> {char_list}")

"""
OUTPUT:
String to Character List Converter
----------------------------------------
'hello' -> ['h', 'e', 'l', 'l', 'o']
'python' -> ['p', 'y', 't', 'h', 'o', 'n']
'123abc' -> ['1', '2', '3', 'a', 'b', 'c']
'' -> []
"""
