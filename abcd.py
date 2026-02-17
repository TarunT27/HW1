word = "MADAM"
reversed = ""

for i in range(len(word) - 1, -1, -1):
    reversed = reversed + word[i]

if reversed == word:
    print("Palindrome")
else:
    print("Not a Palindrome")
