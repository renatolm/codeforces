t = int(input())

words = []
for i in range(t):
    word = []
    for line in range(8):
        line = input()
        for c in line:
            if c!='.':
                word.append(c)
    word = ''.join(word)
    words.append(word)

for word in words:
    print(word)