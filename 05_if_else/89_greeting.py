"""
Program 89: Print "Hello" if input number > 10, else print "Goodbye"
This program demonstrates conditional output.
"""

def conditional_greeting(num):
    """Print greeting based on number"""
    if num > 10:
        return "Hello"
    else:
        return "Goodbye"


# Main program
if __name__ == "__main__":
    test_nums = [5, 10, 15, 0, 20, 11]
    
    print("Conditional Greeter")
    print("-" * 40)
    for num in test_nums:
        result = conditional_greeting(num)
        print(f"{num} -> {result}")

"""
OUTPUT:
Conditional Greeter
----------------------------------------
5 -> Goodbye
10 -> Goodbye
15 -> Hello
0 -> Goodbye
20 -> Hello
11 -> Hello
"""
