n = int(input())

cases = []
for i in range(n):
    cases.append(list(input()))

for case in cases:
    cursor = 1
    count = 0
    for digit in case:        
        if int(digit)==0:
            real_digit = 10
        else:
            real_digit = int(digit)

        if real_digit==cursor:
            count+=1
        else:
            count += abs(cursor-real_digit)+1
            cursor = real_digit
    print(count)