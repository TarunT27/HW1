"""
Program 94: Check if a dictionary is empty
This program validates dictionary emptiness.
"""

def is_dict_empty(d):
    """Check if dictionary is empty"""
    if len(d) == 0:
        return True
    else:
        return False


# Main program
if __name__ == "__main__":
    test_dicts = [
        {},
        {'a': 1},
        {'name': 'John', 'age': 30},
        {None: None},
    ]
    
    print("Dictionary Empty Checker")
    print("-" * 40)
    for d in test_dicts:
        result = is_dict_empty(d)
        print(f"{d} -> Empty: {result}")

"""
OUTPUT:
Dictionary Empty Checker
----------------------------------------
{} -> Empty: True
{'a': 1} -> Empty: False
{'name': 'John', 'age': 30} -> Empty: False
{None: None} -> Empty: False
"""
