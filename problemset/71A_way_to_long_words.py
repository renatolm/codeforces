# input reading
n = int(input())

words = []
for i in range(n):
    words.append(input())
    

# solution
for word in words:
    if len(word)>10:
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)