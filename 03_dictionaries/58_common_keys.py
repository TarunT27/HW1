# Common keys
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 20, 'c': 30, 'd': 40}
common = list(set(d1.keys()) & set(d2.keys()))
print("Common keys:", common)
