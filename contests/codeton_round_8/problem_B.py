def mex(arr):
    mini = 0
    found = False
    
    while found is False:        
        if mini not in arr:
            found = True
        else:
            mini+=1

    return mini

t = int(input())

cases = []
for i in range(t):
    n = input()
    line = input().split(' ')
    cases.append([int(x) for x in line])    

for case in cases:
    result = []    

    for ele in case:
        for p in range(len(case)):
            if p not in result:                
                if mex(result+[p])-p==ele:
                    result.append(p)
                    break

    print(' '.join([str(x) for x in result]))