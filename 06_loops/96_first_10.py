"""
Program 96: Print the first 10 natural numbers using a loop
This program demonstrates basic loop iteration.
"""

def print_first_10():
    """Print first 10 natural numbers"""
    for i in range(1, 11):
        print(i, end=" ")
    print()


# Main program
if __name__ == "__main__":
    print("First 10 Natural Numbers")
    print("-" * 40)
    print_first_10()

"""
OUTPUT:
First 10 Natural Numbers
----------------------------------------
1 2 3 4 5 6 7 8 9 10
"""
