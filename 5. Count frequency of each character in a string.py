'''n = input()
freq = {}

for i in n:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for char, count in freq.items():
    print(char, ":", count)'''



s="sasi"
frequency = {}
for i in s:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
for char, count in freq.items():
    print(char, ":", count)
