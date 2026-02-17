"""
Program 16: Check if two strings are rotations of each other
A string is a rotation of another if it appears as a substring
when the original is doubled.
"""

def are_rotations(str1, str2):
    """Check if two strings are rotations of each other"""
    # Strings must be same length to be rotations
    if len(str1) != len(str2):
        return False
    # Check if str2 is a substring of str1 + str1
    return str2 in str1 + str1


# Main program
if __name__ == "__main__":
    test_cases = [
        ("abcd", "acbd"),
        ("abcd", "cdab"),
        ("abcd", "dabc"),
        ("hello", "llohe"),
        ("python", "thonpy")
    ]
    
    print("String Rotation Checker")
    print("-" * 40)
    for str1, str2 in test_cases:
        result = are_rotations(str1, str2)
        print(f"'{str1}' and '{str2}' are rotations -> {result}")

"""
OUTPUT:
String Rotation Checker
----------------------------------------
'abcd' and 'acbd' are rotations -> False
'abcd' and 'cdab' are rotations -> True
'abcd' and 'dabc' are rotations -> True
'hello' and 'llohe' are rotations -> True
'python' and 'thonpy' are rotations -> True
"""
