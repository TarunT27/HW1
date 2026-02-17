"""
Program 151: Find duplicate characters in a string
This program identifies which characters appear more than once in a string.
"""

def find_duplicates(s):
    """Find duplicate characters"""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return {char: count for char, count in freq.items() if count > 1}


# Main program
if __name__ == "__main__":
    test_cases = [
        "hello",
        "programming",
        "aabbcc",
        "xyz",
    ]
    
    print("Find Duplicate Characters")
    print("-" * 40)
    for s in test_cases:
        duplicates = find_duplicates(s)
        print(f"String: {s}")
        print(f"Duplicates: {duplicates}\n")

"""
OUTPUT:
Find Duplicate Characters
----------------------------------------
String: hello
Duplicates: {'l': 2}

String: programming
Duplicates: {'r': 2, 'g': 2, 'm': 2}

String: aabbcc
Duplicates: {'a': 2, 'b': 2, 'c': 2}

String: xyz
Duplicates: {}
"""
