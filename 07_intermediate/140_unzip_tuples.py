# Unzip list of tuples
tuples = [(1, "a"), (2, "b"), (3, "c")]
unzipped = list(zip(*tuples))

print(unzipped)
