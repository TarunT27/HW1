"""
Program 102: Print multiplication table of a given number using a loop
This program generates multiplication table.
"""

def multiplication_table(num, limit=10):
    """Generate multiplication table"""
    table = []
    for i in range(1, limit + 1):
        table.append(num * i)
    return table


# Main program
if __name__ == "__main__":
    test_nums = [2, 5, 7]
    
    print("Multiplication Table Generator")
    print("-" * 40)
    for num in test_nums:
        table = multiplication_table(num)
        print(f"Table of {num}:")
        for i, product in enumerate(table, 1):
            print(f"  {num} x {i} = {product}")
        print()

"""
OUTPUT:
Multiplication Table Generator
----------------------------------------
Table of 2:
  2 x 1 = 2
  2 x 2 = 4
  2 x 3 = 6
  2 x 4 = 8
  2 x 5 = 10
  2 x 6 = 12
  2 x 7 = 14
  2 x 8 = 16
  2 x 9 = 18
  2 x 10 = 20

Table of 5:
  5 x 1 = 5
  5 x 2 = 10
  5 x 3 = 15
  5 x 4 = 20
  5 x 5 = 25
  5 x 6 = 30
  5 x 7 = 35
  5 x 8 = 40
  5 x 9 = 45
  5 x 10 = 50

Table of 7:
  7 x 1 = 7
  7 x 2 = 14
  7 x 3 = 21
  7 x 4 = 28
  7 x 5 = 35
  7 x 6 = 42
  7 x 7 = 49
  7 x 8 = 56
  7 x 9 = 63
  7 x 10 = 70
"""
