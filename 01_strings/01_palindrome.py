# Check if a string is a palindrome
s = input("Enter a string: ")
s_clean = s.replace(" ", "").lower()

if s_clean == s_clean[::-1]:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")
