"""
Program 27: Find the second largest number in a list
This program identifies the second maximum value.
"""

def find_second_largest(lst):
    """Find second largest number in a list"""
    if len(lst) < 2:
        return None
    
    # Sort and get second last element
    sorted_lst = []
    for num in lst:
        sorted_lst.append(num)
    sorted_lst.sort(reverse=True)
    
    # Remove duplicates of largest and find second largest
    largest = sorted_lst[0]
    for num in sorted_lst:
        if num != largest:
            return num
    return None


# Main program
if __name__ == "__main__":
    test_lists = [
        [5, 2, 8, 1, 9],
        [10, 20, 30],
        [5, 5, 5],
        [1, 2],
        [42]
    ]
    
    print("Second Largest Finder")
    print("-" * 40)
    for lst in test_lists:
        second = find_second_largest(lst)
        print(f"{lst} -> Second Largest: {second}")

"""
OUTPUT:
Second Largest Finder
----------------------------------------
[5, 2, 8, 1, 9] -> Second Largest: 8
[10, 20, 30] -> Second Largest: 20
[5, 5, 5] -> Second Largest: None
[1, 2] -> Second Largest: 1
[42] -> Second Largest: None
"""
