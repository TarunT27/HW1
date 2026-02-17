# Generate combinations
from itertools import combinations

lst = [1, 2, 3, 4]
r = 2

combs = list(combinations(lst, r))
for comb in combs:
    print(comb)
