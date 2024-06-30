n = int(input())

cases = []
for i in range(n):
    cases.append([int(k) for k in input().split(' ')])

for case in cases:
    if case[0]<case[1] and case[1]<case[2]:
        print("STAIR")
    elif case[0]<case[1] and case[1]>case[2]:
        print("PEAK")
    else:
        print("NONE")