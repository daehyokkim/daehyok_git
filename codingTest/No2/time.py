hour = int(input())
result = 0
for hour in range(hour+1):
    for mint in range(60):
        for sec in range(60):
            if '3'in str(hour) + str(mint) + str(sec):
                result+=1

    print(hour)
print(result)