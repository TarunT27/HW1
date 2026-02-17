"""
Program 7: Check if a string is an anagram of another string
Anagrams are words that contain the same letters in different order.
"""

def is_anagram(str1, str2):
    """Check if two strings are anagrams"""
    # Remove spaces and convert to lowercase for comparison
    str1_clean = str1.replace(" ", "").lower()
    str2_clean = str2.replace(" ", "").lower()
    
    # Sort characters and compare
    return sorted(str1_clean) == sorted(str2_clean)


# Main program
if __name__ == "__main__":
    pairs = [
        ("listen", "silent"),
        ("hello", "world"),
        ("abc", "bca"),
        ("Dormitory", "Dirty room"),
        ("python", "typhon")
    ]
    
    print("Anagram Checker")
    print("-" * 40)
    for str1, str2 in pairs:
        result = is_anagram(str1, str2)
        print(f"'{str1}' & '{str2}' -> {result}")

"""
OUTPUT:
Anagram Checker
----------------------------------------
'listen' & 'silent' -> True
'hello' & 'world' -> False
'abc' & 'bca' -> True
'Dormitory' & 'Dirty room' -> True
'python' & 'typhon' -> True
"""
