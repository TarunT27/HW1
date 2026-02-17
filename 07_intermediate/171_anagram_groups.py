"""
Program 171: Group anagrams together
This program groups strings that are anagrams of each other.
"""

def group_anagrams(strings):
    """Group anagrams"""
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagram_dict:
            anagram_dict[sorted_s] = []
        anagram_dict[sorted_s].append(s)
    return list(anagram_dict.values())


# Main program
if __name__ == "__main__":
    test_cases = [
        ["listen", "silent", "hello", "world"],
        ["eat", "tea", "ate", "bat"],
        ["a", "b", "c"],
    ]
    
    print("Anagram Grouper")
    print("-" * 40)
    for strings in test_cases:
        groups = group_anagrams(strings)
        print(f"Strings: {strings}")
        print(f"Groups: {groups}\n")

"""
OUTPUT:
Anagram Grouper
----------------------------------------
Strings: ['listen', 'silent', 'hello', 'world']
Groups: [['listen', 'silent'], ['hello'], ['world']]

Strings: ['eat', 'tea', 'ate', 'bat']
Groups: [['eat', 'tea', 'ate'], ['bat']]

Strings: ['a', 'b', 'c']
Groups: [['a'], ['b'], ['c']]
"""
