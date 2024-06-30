n = int(input())

cases = []
for i in range(n):
    cases.append(int(input()))

for case in cases:
    even_line = ""
    odd_line = ""
    for k in range(case):
        if k%2==0:
            even_line+="##"
            odd_line+=".."
        else:
            even_line+=".."
            odd_line+="##"


    even=True
    for j in range(case):
        if even is True:
            print(even_line)
            print(even_line)
            even=False
        else:
            print(odd_line)
            print(odd_line)
            even=True