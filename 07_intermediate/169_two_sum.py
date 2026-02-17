"""
Program 169: Two sum problem - find two numbers that add to target
This program finds the indices of two numbers that sum to a target value.
"""

def two_sum(lst, target):
    """Find two numbers that sum to target"""
    seen = {}
    for i, num in enumerate(lst):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Main program
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    
    print("Two Sum Problem")
    print("-" * 40)
    for lst, target in test_cases:
        result = two_sum(lst, target)
        print(f"List: {lst}, Target: {target}")
        if result:
            print(f"Indices: {result}, Values: [{lst[result[0]]}, {lst[result[1]]}]")
        else:
            print(f"No solution found")
        print()

"""
OUTPUT:
Two Sum Problem
----------------------------------------
List: [2, 7, 11, 15], Target: 9
Indices: [0, 1], Values: [2, 7]

List: [3, 2, 4], Target: 6
Indices: [1, 2], Values: [2, 4]

List: [3, 3], Target: 6
Indices: [0, 1], Values: [3, 3]
"""
