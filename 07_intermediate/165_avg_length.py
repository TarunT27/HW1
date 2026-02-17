"""
Program 165: Calculate average string length in list
This program computes the average length of strings in a list.
"""

def average_string_length(strings):
    """Calculate average string length"""
    if not strings:
        return 0
    return sum(len(s) for s in strings) / len(strings)


# Main program
if __name__ == "__main__":
    test_cases = [
        ["hello", "world"],
        ["a", "bb", "ccc"],
        ["python", "is", "awesome"],
    ]
    
    print("Average String Length Calculator")
    print("-" * 40)
    for strings in test_cases:
        avg = average_string_length(strings)
        print(f"Strings: {strings}")
        print(f"Average length: {avg:.2f}\n")

"""
OUTPUT:
Average String Length Calculator
----------------------------------------
Strings: ['hello', 'world']
Average length: 5.00

Strings: ['a', 'bb', 'ccc']
Average length: 2.00

Strings: ['python', 'is', 'awesome']
Average length: 5.00
"""
