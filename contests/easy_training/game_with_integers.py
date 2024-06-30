n = int(input())

cases = []
for i in range(n):
    cases.append(int(input()))

for case in cases:
    if (case+1)%3==0 or (case-1)%3==0:
        print("First")
    else:
        print("Second")