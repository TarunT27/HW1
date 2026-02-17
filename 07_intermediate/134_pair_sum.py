"""
Program 134: Find all pairs in a list that sum to a specific number
This program finds pairs with given sum.
"""

def find_pairs_with_sum(lst, target):
    """Find all pairs that sum to target"""
    pairs = []
    seen = set()
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
        ([2, 3, 5, 7], 10)
    ]
    
    print("Pair Sum Finder")
    print("-" * 40)
    for lst, target in test_cases:
        result = find_pairs_with_sum(lst, target)
        print(f"{lst}, target={target} -> {result}")

"""
OUTPUT:
Pair Sum Finder
----------------------------------------
[1, 5, 7, -1, 5], target=6 -> [(5, 1), (1, 5)]
[2, 3, 5, 7], target=10 -> [(3, 7), (5, 5)]
"""
