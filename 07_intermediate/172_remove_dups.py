"""
Program 172: Remove all duplicates from list keeping order
This program removes duplicate elements while maintaining original order.
"""

def remove_duplicates_ordered(lst):
    """Remove duplicates preserving order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Main program
if __name__ == "__main__":
    test_cases = [
        [1, 2, 2, 3, 3, 3],
        ['a', 'b', 'a', 'c'],
        [1, 1, 1, 1],
    ]
    
    print("Remove Duplicates (Ordered)")
    print("-" * 40)
    for lst in test_cases:
        result = remove_duplicates_ordered(lst)
        print(f"Original: {lst}")
        print(f"Result: {result}\n")

"""
OUTPUT:
Remove Duplicates (Ordered)
----------------------------------------
Original: [1, 2, 2, 3, 3, 3]
Result: [1, 2, 3]

Original: ['a', 'b', 'a', 'c']
Result: ['a', 'b', 'c']

Original: [1, 1, 1, 1]
Result: [1]
"""
