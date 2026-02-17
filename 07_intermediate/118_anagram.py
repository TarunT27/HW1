# Check anagram
s1 = input("Enter string 1: ").replace(" ", "").lower()
s2 = input("Enter string 2: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not anagram")
