"""
Program 170: String compression - compress consecutive characters
This program compresses a string by counting consecutive characters.
"""

def compress_string(s):
    """Compress string"""
    if not s:
        return ""
    
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    
    result = ''.join(compressed)
    return result if len(result) < len(s) else s


# Main program
if __name__ == "__main__":
    test_cases = [
        "aabbcc",
        "abcdef",
        "aaaaaaa",
    ]
    
    print("String Compressor")
    print("-" * 40)
    for s in test_cases:
        compressed = compress_string(s)
        print(f"Original: {s}")
        print(f"Compressed: {compressed}\n")

"""
OUTPUT:
String Compressor
----------------------------------------
Original: aabbcc
Compressed: a2b2c2

Original: abcdef
Compressed: abcdef

Original: aaaaaaa
Compressed: a7
"""
