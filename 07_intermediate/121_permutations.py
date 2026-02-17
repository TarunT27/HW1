# Generate permutations of list
lst = [1, 2, 3]
from itertools import permutations

perms = list(permutations(lst))
for perm in perms:
    print(perm)
