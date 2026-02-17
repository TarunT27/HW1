"""
Program 109: Calculate the product of all elements in a list using a loop
This program multiplies all list elements.
"""

def product_loop(lst):
    """Calculate product using loop"""
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
        [1, 1, 1],
        [5, 2]
    ]
    
    print("Product Calculator (using loop)")
    print("-" * 40)
    for lst in test_lists:
        product = product_loop(lst)
        print(f"{lst} -> Product: {product}")

"""
OUTPUT:
Product Calculator (using loop)
----------------------------------------
[1, 2, 3, 4, 5] -> Product: 120
[2, 3, 4] -> Product: 24
[10] -> Product: 10
[1, 1, 1] -> Product: 1
[5, 2] -> Product: 10
"""
