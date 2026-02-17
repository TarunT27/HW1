# Check if string contains vowel
s = input("Enter string: ")
vowels = "aeiouAEIOU"
found = False

for char in s:
    if char in vowels:
        found = True
        break

if found:
    print("Contains vowel")
else:
    print("No vowel")
