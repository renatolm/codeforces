t = int(input())

cases = []
for i in range(t):        
    line = input().split(' ')
    n, k = int(line[0]), int(line[1])
    rating = [int(i) for i in input().split(' ')]
    cases.append({'n':n, 'k':k, 'rating':rating})

for case in cases:
    my_rating = case['rating'][case['k']-1]
    wins=0

    before_bigger = 0
    after_bigger = 0
    found_bigger = 0    
    for i in range(k):        

        if case['rating'][i]>my_rating:
            found_bigger += 1

        if case['rating'][i]>my_rating and found_bigger==2:
            break
        
        elif case['rating'][i]<my_rating and found_bigger==0:
            before_bigger+=1

        elif case['rating'][i]<my_rating and found_bigger==1:
            after_bigger+=1    

    wins = max([wins,before_bigger,after_bigger])
    print(wins)