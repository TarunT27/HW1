"""
Program 120: Reverse the words in a given sentence
This program reverses word order in sentence.
"""

def reverse_sentence(s):
    """Reverse words in a sentence"""
    words = s.split()
    return " ".join(reversed(words))


# Main program
if __name__ == "__main__":
    test_sentences = [
        "Hello World Python",
        "The quick brown fox",
        "A",
        ""
    ]
    
    print("Sentence Word Reverser")
    print("-" * 40)
    for s in test_sentences:
        result = reverse_sentence(s)
        print(f"'{s}' -> '{result}'")

"""
OUTPUT:
Sentence Word Reverser
----------------------------------------
'Hello World Python' -> 'Python World Hello'
'The quick brown fox' -> 'fox brown quick The'
'A' -> 'A'
'' -> ''
"""
