# Find longest substring without repeating
s = input("Enter string: ")
max_len = 0
max_sub = ""

for i in range(len(s)):
    seen = set()
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
    if len(seen) > max_len:
        max_len = len(seen)
        max_sub = s[i:i+max_len]

print("Longest:", max_sub)
