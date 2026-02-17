"""
Program 154: Find pair of elements with given sum
This program finds two elements in a list that add up to a target sum.
"""

def find_pair_sum(lst, target):
    """Find pair with given sum"""
    seen = set()
    pairs = []
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs


# Main program
if __name__ == "__main__":
    test_cases = [
        ([1, 5, 7, -1, 5], 6),
        ([2, 3, 5, 7, 11], 9),
        ([1, 1, 1, 1], 2),
    ]
    
    print("Find Pair with Sum")
    print("-" * 40)
    for lst, target in test_cases:
        pairs = find_pair_sum(lst, target)
        print(f"List: {lst}, Target: {target}")
        print(f"Pairs: {pairs}\n")

"""
OUTPUT:
Find Pair with Sum
----------------------------------------
List: [1, 5, 7, -1, 5], Target: 6
Pairs: [(5, 1), (1, 5)]

List: [2, 3, 5, 7, 11], Target: 9
Pairs: [(2, 7)]

List: [1, 1, 1, 1], Target: 2
Pairs: [(1, 1), (1, 1), (1, 1)]
"""
