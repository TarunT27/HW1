"""
Program 136: Split a list into chunks of size n
This program divides list into fixed-size chunks.
"""

def split_into_chunks(lst, n):
    """Split list into chunks of size n"""
    chunks = []
    for i in range(0, len(lst), n):
        chunks.append(lst[i:i+n])
    return chunks


# Main program
if __name__ == "__main__":
    test_cases = [([1,2,3,4,5,6], 2), (['a','b','c','d','e'], 2)]
    
    print("Chunk Splitter")
    print("-" * 40)
    for lst, n in test_cases:
        result = split_into_chunks(lst, n)
        print(f"{lst}, chunk_size={n} -> {result}")

"""
OUTPUT:
Chunk Splitter
----------------------------------------
[1, 2, 3, 4, 5, 6], chunk_size=2 -> [[1, 2], [3, 4], [5, 6]]
['a', 'b', 'c', 'd', 'e'], chunk_size=2 -> [['a', 'b'], ['c', 'd'], ['e']]
"""
