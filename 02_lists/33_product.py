"""
Program 33: Find the product of elements in a list
This program multiplies all numbers together.
"""

def product_of_elements(lst):
    """Find product of all elements in a list"""
    if not lst:
        return 1
    product = 1
    for num in lst:
        product *= num
    return product


# Main program
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4, 5],
        [2, 3, 4],
        [10],
        [0, 5, 10],
        [1, 1, 1, 1]
    ]
    
    print("Product of Elements Calculator")
    print("-" * 40)
    for lst in test_lists:
        product = product_of_elements(lst)
        print(f"{lst} -> Product: {product}")

"""
OUTPUT:
Product of Elements Calculator
----------------------------------------
[1, 2, 3, 4, 5] -> Product: 120
[2, 3, 4] -> Product: 24
[10] -> Product: 10
[0, 5, 10] -> Product: 0
[1, 1, 1, 1] -> Product: 1
"""
