n = int(input())

cases = []
for i in range(n):
    cases.append([int(k) for k in input().split(' ')])

for case in cases:
    height = 0
    a = case[0]
    b = case[1]
    c = case[2]    

    next_available = 1
    remaining = False
    while next_available>0:
        available = next_available
        next_available = 0
        if a>0 and available>0:            
            how_many_a = min(available, a) 
            a -= how_many_a
            available -= how_many_a
            next_available += 2*how_many_a        

        if b>0 and available>0:
            how_many_b = min(available, b)
            b -= how_many_b
            available -= how_many_b
            next_available += how_many_b
            

        if c>0 and available>0:
            how_many_c = min(available, c)
            c -= how_many_c
            available -= how_many_c            

        height+=1
        if available>0:
            remaining = True
            next_available=0

    if a+b+c>0 or remaining is True:
        print(-1)
    else:
        print(height-1)