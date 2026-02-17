"""
Program 144: Find longest increasing subsequence
This program finds the longest subsequence of elements that are in increasing order.
"""

def longest_increasing_subsequence(lst):
    """Find longest increasing subsequence"""
    if not lst:
        return []
    
    n = len(lst)
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if lst[j] < lst[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    lis = []
    idx = max_index
    while idx != -1:
        lis.append(lst[idx])
        idx = parent[idx]
    lis.reverse()
    
    return lis


# Main program
if __name__ == "__main__":
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 4, 4, 4, 3, 5, 9, 7, 40],
        [1, 2, 3],
    ]
    
    print("Longest Increasing Subsequence Finder")
    print("-" * 40)
    for lst in test_cases:
        result = longest_increasing_subsequence(lst)
        print(f"List: {lst}")
        print(f"LIS: {result}")
        print(f"Length: {len(result)}\n")

"""
OUTPUT:
Longest Increasing Subsequence Finder
----------------------------------------
List: [10, 9, 2, 5, 3, 7, 101, 18]
LIS: [2, 3, 7, 18]
Length: 4

List: [0, 1, 0, 4, 4, 4, 3, 5, 9, 7, 40]
LIS: [0, 1, 4, 5, 9, 40]
Length: 6

List: [1, 2, 3]
LIS: [1, 2, 3]
Length: 3
"""
