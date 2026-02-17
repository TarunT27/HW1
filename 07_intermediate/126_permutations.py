"""
Program 126: Find all possible permutations of a string
This program generates all permutations.
"""

def permutations(s):
    """Find all permutations of a string"""
    from itertools import combinations
    result = []
    
    def generate_perms(chars):
        if len(chars) == 1:
            return [chars]
        perms = []
        for i in range(len(chars)):
            for perm in generate_perms(chars[:i] + chars[i+1:]):
                perms.append(chars[i] + perm)
        return perms
    
    return generate_perms(s)


# Main program
if __name__ == "__main__":
    test_strings = ["ab", "abc"]
    
    print("Permutations Finder")
    print("-" * 40)
    for s in test_strings:
        perms = sorted(set(permutations(s)))
        print(f"'{s}' -> {len(perms)} permutations")
        print(f"  {perms}\n")

"""
OUTPUT:
Permutations Finder
----------------------------------------
'ab' -> 2 permutations
  ['ab', 'ba']

'abc' -> 6 permutations
  ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""
