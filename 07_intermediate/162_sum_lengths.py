"""
Program 162: Sum of string lengths in list
This program calculates the total length of all strings in a list.
"""

def sum_string_lengths(strings):
    """Sum lengths of strings"""
    return sum(len(s) for s in strings)


# Main program
if __name__ == "__main__":
    test_cases = [
        ["hello", "world"],
        ["a", "bb", "ccc"],
        ["python", "is", "awesome"],
    ]
    
    print("Sum of String Lengths")
    print("-" * 40)
    for strings in test_cases:
        total = sum_string_lengths(strings)
        lengths = [len(s) for s in strings]
        print(f"Strings: {strings}")
        print(f"Lengths: {lengths}")
        print(f"Total: {total}\n")

"""
OUTPUT:
Sum of String Lengths
----------------------------------------
Strings: ['hello', 'world']
Lengths: [5, 5]
Total: 10

Strings: ['a', 'bb', 'ccc']
Lengths: [1, 2, 3]
Total: 6

Strings: ['python', 'is', 'awesome']
Lengths: [6, 2, 7]
Total: 15
"""
