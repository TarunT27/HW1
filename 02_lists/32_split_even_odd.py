"""
Program 32: Split a list into even and odd numbers
This program separates even and odd numbers into different lists.
"""

def split_even_odd(lst):
    """Split list into even and odd numbers"""
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5, 6],
        [10, 15, 20, 25],
        [2, 4, 6, 8],
        [1, 3, 5, 7],
        []
    ]
    
    print("Even/Odd Splitter")
    print("-" * 40)
    for lst in test_lists:
        even, odd = split_even_odd(lst)
        print(f"{lst}")
        print(f"  Even: {even}, Odd: {odd}\n")

"""
OUTPUT:
Even/Odd Splitter
----------------------------------------
[1, 2, 3, 4, 5, 6]
  Even: [2, 4, 6], Odd: [1, 3, 5]

[10, 15, 20, 25]
  Even: [10, 20], Odd: [15, 25]

[2, 4, 6, 8]
  Even: [2, 4, 6, 8], Odd: []

[1, 3, 5, 7]
  Even: [], Odd: [1, 3, 5, 7]

[]
  Even: [], Odd: []
"""
