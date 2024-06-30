t = int(input())

cases = []
for i in range(t):
    line = input().split(' ')
    cases.append((int(line[0]),int(line[1])))

for case in cases:    
    n = case[0]
    k = case[1]

    if k==1:
        result = [str(x) for x in range(1,n+1)]
        print(' '.join(result))
    elif k==n:
        print(' '.join([str(1)]*n))
    else:
        print(-1)