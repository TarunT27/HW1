# Split list into chunks
lst = [1, 2, 3, 4, 5, 6, 7, 8]
chunk_size = 3
chunks = [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

print(chunks)
