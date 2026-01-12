vowels = ['a', 'e', 'i', 'o', 'u']

user = input("Enter a word: ").lower()

has_vowel = False
for ch in user:
    if ch in vowels:
        has_vowel = True
        break

if has_vowel:
    print("Has vowels")
else:
    print("Does not")
