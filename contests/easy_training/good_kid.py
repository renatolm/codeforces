n_test_cases = int(input())

test_cases = []
for i in range(n_test_cases):
    n = int(input())
    test_cases.append([int(k) for k in input().split(' ')])

for case in test_cases:
    prod=1
    mini=min(case)
    count_replacement=0
    for num in case:
        if num==mini and count_replacement==0:
            count_replacement+=1
            prod = prod*(num+1)
        else:
            prod = prod*num        
    
    print(int(prod))
