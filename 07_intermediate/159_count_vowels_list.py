"""
Program 159: Count total vowels in list of strings
This program counts the total number of vowels across all strings in a list.
"""

def count_vowels_in_list(strings):
    """Count vowels in list of strings"""
    vowels = 'aeiouAEIOU'
    total = 0
    for s in strings:
        for char in s:
            if char in vowels:
                total += 1
    return total


# Main program
if __name__ == "__main__":
    test_cases = [
        ["hello", "world"],
        ["python", "programming", "language"],
        ["code", "data", "science"],
    ]
    
    print("Count Vowels in String List")
    print("-" * 40)
    for strings in test_cases:
        count = count_vowels_in_list(strings)
        print(f"Strings: {strings}")
        print(f"Total vowels: {count}\n")

"""
OUTPUT:
Count Vowels in String List
----------------------------------------
Strings: ['hello', 'world']
Total vowels: 3

Strings: ['python', 'programming', 'language']
Total vowels: 6

Strings: ['code', 'data', 'science']
Total vowels: 7
"""
