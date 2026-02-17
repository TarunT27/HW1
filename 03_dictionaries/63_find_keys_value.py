# Find keys with value
d = {'a': 1, 'b': 2, 'c': 1}
value = 1
keys = [k for k, v in d.items() if v == value]
print("Keys with value", value + ":", keys)
