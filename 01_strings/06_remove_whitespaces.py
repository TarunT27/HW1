"""
Program 6: Remove all whitespaces from a string
This program removes spaces, tabs, and newlines from a string.
"""

def remove_whitespaces(s):
    """Remove all whitespaces from a string"""
    return s.replace(" ", "").replace("\t", "").replace("\n", "")


def remove_whitespaces_join(s):
    """Remove whitespaces using join and split"""
    return "".join(s.split())


# Main program
if __name__ == "__main__":
    test_strings = ["Hello World", "Python Programming", "a b c d", "NoSpaces"]
    
    print("Whitespace Remover")
    print("-" * 40)
    for test in test_strings:
        result = remove_whitespaces(test)
        print(f"'{test}' -> '{result}'")

"""
OUTPUT:
Whitespace Remover
----------------------------------------
'Hello World' -> 'HelloWorld'
'Python Programming' -> 'PythonProgramming'
'a b c d' -> 'abcd'
'NoSpaces' -> 'NoSpaces'
"""
