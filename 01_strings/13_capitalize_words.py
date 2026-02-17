"""
Program 13: Capitalize the first letter of each word in a string
This program converts the first letter of each word to uppercase.
"""

def capitalize_words(s):
    """Capitalize first letter of each word using title()"""
    return s.title()


def capitalize_words_manual(s):
    """Capitalize first letter of each word manually"""
    words = s.split()
    capitalized_words = []
    for word in words:
        if word:
            capitalized_word = word[0].upper() + word[1:]
            capitalized_words.append(capitalized_word)
    return " ".join(capitalized_words)


# Main program
if __name__ == "__main__":
    test_strings = ["hello world", "python programming", "i love python", "HELLO WORLD"]
    
    print("Word Capitalizer")
    print("-" * 40)
    for test in test_strings:
        result = capitalize_words(test)
        print(f"'{test}' -> '{result}'")

"""
OUTPUT:
Word Capitalizer
----------------------------------------
'hello world' -> 'Hello World'
'python programming' -> 'Python Programming'
'i love python' -> 'I Love Python'
'HELLO WORLD' -> 'Hello World'
"""
