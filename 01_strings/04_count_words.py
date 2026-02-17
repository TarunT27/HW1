"""
Program 4: Count the number of words in a string
This program counts the number of words separated by spaces.
"""

def count_words(s):
    """Count the number of words in a string"""
    if not s.strip():  # Handle empty or whitespace-only strings
        return 0
    return len(s.split())


def count_words_manual(s):
    """Count words manually without split()"""
    if not s.strip():
        return 0
    word_count = 1
    for char in s:
        if char == " ":
            word_count += 1
    return word_count


# Main program
if __name__ == "__main__":
    test_strings = ["Hello World", "Python is awesome", "OneWord", "   ", "", "The quick brown fox"]
    
    print("Word Counter")
    print("-" * 40)
    for test in test_strings:
        count = count_words(test)
        print(f"'{test}' -> {count} words")

"""
OUTPUT:
Word Counter
----------------------------------------
'Hello World' -> 2 words
'Python is awesome' -> 3 words
'OneWord' -> 1 words
'   ' -> 0 words
'' -> 0 words
'The quick brown fox' -> 4 words
"""
