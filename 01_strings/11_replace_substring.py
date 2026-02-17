"""
Program 11: Replace all occurrences of a substring in a string
This program replaces all instances of a substring with another.
"""

def replace_substring(s, old, new):
    """Replace all occurrences of a substring"""
    return s.replace(old, new)


def replace_substring_manual(s, old, new):
    """Replace substring manually without built-in replace()"""
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        ("Hello World", "World", "Python"),
        ("banana", "a", "o"),
        ("aaa", "aa", "b"),
        ("hello world hello", "hello", "hi")
    ]
    
    print("Substring Replacer")
    print("-" * 40)
    for string, old, new in test_cases:
        result = replace_substring(string, old, new)
        print(f"'{string}'")
        print(f"  Replace '{old}' with '{new}' -> '{result}'\n")

"""
OUTPUT:
Substring Replacer
----------------------------------------
'Hello World'
  Replace 'World' with 'Python' -> 'Hello Python'

'banana'
  Replace 'a' with 'o' -> 'bonono'

'aaa'
  Replace 'aa' with 'b' -> 'ba'

'hello world hello'
  Replace 'hello' with 'hi' -> 'hi world hi'
"""
