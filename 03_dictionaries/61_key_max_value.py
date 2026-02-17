# Key with max value
d = {'a': 10, 'b': 5, 'c': 20}
key = max(d, key=d.get)
print("Key with max value:", key)
