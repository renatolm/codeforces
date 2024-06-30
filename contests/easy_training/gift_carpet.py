t = int(input())

carpets = []
for i in range(t):    
    input_line = input()
    n, m = (int(k) for k in input_line.split(' '))
    carpet = []
    for line in range(n):
        carpet.append(list(input()))
    carpets.append(carpet)

name = ['v','i','k','a']
for carpet in carpets:
    if len(carpet[0])<4:
        print("NO")
    else:
        search_letter=0
        found=False
        for col in range(len(carpet[0])):
            for row in range(len(carpet)):                
                if carpet[row][col]==name[search_letter]:
                    search_letter+=1        
                    break
            if search_letter==4:
                found = True                
                break
        if found:
            print("YES")
        else:
            print("NO")