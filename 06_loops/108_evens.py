"""
Program 108: Print all even numbers from 1 to 100 using a loop
This program prints even numbers.
"""

def evens_up_to(limit):
    """Get all even numbers up to limit"""
    evens = []
    for i in range(2, limit + 1, 2):
        evens.append(i)
    return evens


# Main program
if __name__ == "__main__":
    print("Even Numbers from 1 to 100")
    print("-" * 40)
    evens = evens_up_to(100)
    print(evens)

"""
OUTPUT:
Even Numbers from 1 to 100
----------------------------------------
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
"""
