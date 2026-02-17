# Word frequency
s = "hello world hello"
words = s.lower().split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Frequency:", freq)
