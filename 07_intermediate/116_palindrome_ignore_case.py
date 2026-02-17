# Check palindrome ignoring spaces and case
s = input("Enter string: ").replace(" ", "").lower()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
