"""
Program 164: Count total characters in list of strings
This program counts the total number of characters across all strings.
"""

def total_char_count(strings):
    """Count total characters"""
    return sum(len(s) for s in strings)


# Main program
if __name__ == "__main__":
    test_cases = [
        ["hello", "world"],
        ["a", "bb", "ccc", "dddd"],
        ["python", "java", "cpp"],
    ]
    
    print("Total Character Counter")
    print("-" * 40)
    for strings in test_cases:
        total = total_char_count(strings)
        print(f"Strings: {strings}")
        print(f"Total chars: {total}\n")

"""
OUTPUT:
Total Character Counter
----------------------------------------
Strings: ['hello', 'world']
Total chars: 10

Strings: ['a', 'bb', 'ccc', 'dddd']
Total chars: 10

Strings: ['python', 'java', 'cpp']
Total chars: 12
"""
