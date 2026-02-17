"""
Program 123: Find number of uppercase and lowercase letters in a string
This program counts letter cases.
"""

def count_case_letters(s):
    """Count uppercase and lowercase letters"""
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower


# Main program
if __name__ == "__main__":
    test_strings = [
        "Hello World",
        "PYTHON",
        "python",
        "HeLLo WoRLd",
        "123abc"
    ]
    
    print("Case Letter Counter")
    print("-" * 40)
    for s in test_strings:
        upper, lower = count_case_letters(s)
        print(f"'{s}' -> Upper: {upper}, Lower: {lower}")

"""
OUTPUT:
Case Letter Counter
----------------------------------------
'Hello World' -> Upper: 2, Lower: 8
'PYTHON' -> Upper: 6, Lower: 0
'python' -> Upper: 0, Lower: 6
'HeLLo WoRLd' -> Upper: 5, Lower: 5
'123abc' -> Upper: 0, Lower: 3
"""
