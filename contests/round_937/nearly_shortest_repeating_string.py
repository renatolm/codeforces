def difference(str1, str2):
    count=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            count+=1
        if count>1:
            return count
    return count

n = int(input())

cases = []
for i in range(n):
    x = input()
    cases.append(input())

for case in cases:
    
    found = False
    for size in range(1,int(len(case)/2)+1):        
        found = False
        if len(case)%size==0:
            for k in range(int(len(case)/size)):
                subs = case[size*k:(k+1)*size]
                compare = subs*int(len(case)/size)
                count = difference(compare, case)                                
                if count<2:
                    found = True
                    break                
            if found is True:
                break        

    if found is True:
        print(len(subs))
    else:
        print(len(case))