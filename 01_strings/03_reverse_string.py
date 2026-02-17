"""
Program 3: Reverse a string
This program reverses the input string using slicing.
"""

def reverse_string(s):
    """Reverse a string using slicing"""
    return s[::-1]


def reverse_string_loop(s):
    """Reverse a string using a loop"""
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s


# Main program
if __name__ == "__main__":
    test_strings = ["Hello", "Python", "12345", "racecar"]
    
    print("String Reversal")
    print("-" * 40)
    for test in test_strings:
        rev_slicing = reverse_string(test)
        rev_loop = reverse_string_loop(test)
        print(f"Original: '{test}'")
        print(f"Reversed: '{rev_slicing}'\n")

"""
OUTPUT:
String Reversal
----------------------------------------
Original: 'Hello'
Reversed: 'olleH'

Original: 'Python'
Reversed: 'nohtyP'

Original: '12345'
Reversed: '54321'

Original: 'racecar'
Reversed: 'racecar'
"""
