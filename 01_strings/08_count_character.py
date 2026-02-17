"""
Program 8: Count the occurrences of a character in a string
This program counts how many times a specific character appears.
"""

def count_occurrences(s, char):
    """Count occurrences of a character in a string"""
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count


# Main program
if __name__ == "__main__":
    test_cases = [
        ("hello world", "l"),
        ("python", "o"),
        ("mississippi", "s"),
        ("hello", "z"),
        ("aaa", "a")
    ]
    
    print("Character Occurrence Counter")
    print("-" * 40)
    for string, char in test_cases:
        count = count_occurrences(string, char)
        print(f"'{char}' in '{string}' -> {count} times")

"""
OUTPUT:
Character Occurrence Counter
----------------------------------------
'l' in 'hello world' -> 3 times
'o' in 'python' -> 1 times
's' in 'mississippi' -> 4 times
'z' in 'hello' -> 0 times
'a' in 'aaa' -> 3 times
"""
