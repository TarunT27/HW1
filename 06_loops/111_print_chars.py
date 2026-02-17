"""
Program 111: Print all characters in a string using a loop
This program iterates through string characters.
"""

def print_chars(s):
    """Print all characters in a string"""
    for char in s:
        print(char, end=" ")
    print()


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "python", "a"]
    
    print("String Character Printer")
    print("-" * 40)
    for s in test_strings:
        print(f"String: '{s}'")
        print("Characters: ", end="")
        print_chars(s)
        print()

"""
OUTPUT:
String Character Printer
----------------------------------------
String: 'hello'
Characters: h e l l o 

String: 'python'
Characters: p y t h o n 

String: 'a'
Characters: a 
"""
