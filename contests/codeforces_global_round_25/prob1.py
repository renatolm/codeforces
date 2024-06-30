from collections import Counter

t = int(input())

cases = []
for i in range(t):        
    input()
    cases.append(input())

for case in cases:
    c = Counter(case)    
    if c['1']%2!=0:
        print("NO")
    else:
        if len(case)==2:
            print("NO")
        elif len(case)==3:
            if (case[0]=='1' and case[1]=='1') or (case[1]=='1' and case[2]=='1'):
                print("NO")
            else:
                print("YES")
        else:
            print("YES")
