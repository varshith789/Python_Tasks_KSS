#Frequency counter

text = "programming"

freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
