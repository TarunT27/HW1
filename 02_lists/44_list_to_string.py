"""
Program 44: Convert a list of characters into a string
This program joins list elements into a single string.
"""

def list_to_string(char_list):
    """Convert list of characters to string"""
    result = ""
    for char in char_list:
        result += str(char)
    return result


# Main program
if __name__ == "__main__":
    test_lists = [
        ['h', 'e', 'l', 'l', 'o'],
        ['p', 'y', 't', 'h', 'o', 'n'],
        ['a'],
        [],
        ['1', '2', '3']
    ]
    
    print("List to String Converter")
    print("-" * 40)
    for lst in test_lists:
        string = list_to_string(lst)
        print(f"{lst} -> '{string}'")

"""
OUTPUT:
List to String Converter
----------------------------------------
['h', 'e', 'l', 'l', 'o'] -> 'hello'
['p', 'y', 't', 'h', 'o', 'n'] -> 'python'
['a'] -> 'a'
[] -> ''
['1', '2', '3'] -> '123'
"""
