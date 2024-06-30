n = int(input())

cases = []

for i in range(n):
    cases.append(input())

columns=['a','b','c','d','e','f','g','h']
for case in cases:
    column = case[0]
    row = int(case[1])
    for i in range(1,9):
        if i!=row:
            print(column+str(i))
    for col in columns:
        if col!=column:
            print(col+str(row))