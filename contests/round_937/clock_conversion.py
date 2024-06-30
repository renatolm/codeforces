n = int(input())

cases = []
for i in range(n):
    cases.append(input())

for case in cases:
    if int(case[:2])>12:
        period="PM"
        hour = int(case[:2])-12
        if hour<10:
            hour="0"+str(hour)
        else:
            hour=str(hour)
    elif int(case[:2])==12:
        period="PM"
        hour = str(12)
    elif int(case[:2])==0:
        period="AM"
        hour= str(12)
    else:
        period="AM"
        hour = case[:2]

    print(hour+case[2:]+" "+period)