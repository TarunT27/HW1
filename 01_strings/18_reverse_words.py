"""
Program 18: Reverse the order of words in a string
This program reverses word order while maintaining character order within words.
"""

def reverse_word_order(s):
    """Reverse the order of words in a string"""
    words = s.split()
    return " ".join(reversed(words))


def reverse_word_order_manual(s):
    """Reverse word order without reversed()"""
    words = s.split()
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    return " ".join(reversed_words)


# Main program
if __name__ == "__main__":
    test_strings = [
        "Hello World Python",
        "The quick brown fox",
        "I love programming",
        "One"
    ]
    
    print("Word Order Reverser")
    print("-" * 40)
    for test in test_strings:
        result = reverse_word_order(test)
        print(f"'{test}'")
        print(f"  -> '{result}'\n")

"""
OUTPUT:
Word Order Reverser
----------------------------------------
'Hello World Python'
  -> 'Python World Hello'

'The quick brown fox'
  -> 'fox brown quick The'

'I love programming'
  -> 'programming love I'

'One'
  -> 'One'
"""
