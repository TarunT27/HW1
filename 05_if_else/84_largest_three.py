"""
Program 84: Find the largest of three numbers
This program compares three numbers and finds maximum.
"""

def find_largest_three(a, b, c):
    """Find largest of three numbers"""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Main program
if __name__ == "__main__":
    test_cases = [
        (10, 20, 15),
        (5, 5, 5),
        (-1, -5, -3),
        (100, 50, 75),
        (0, 0, 1)
    ]
    
    print("Largest of Three Finder")
    print("-" * 40)
    for a, b, c in test_cases:
        largest = find_largest_three(a, b, c)
        print(f"{a}, {b}, {c} -> Largest: {largest}")

"""
OUTPUT:
Largest of Three Finder
----------------------------------------
10, 20, 15 -> Largest: 20
5, 5, 5 -> Largest: 5
-1, -5, -3 -> Largest: -1
100, 50, 75 -> Largest: 100
0, 0, 1 -> Largest: 1
"""
