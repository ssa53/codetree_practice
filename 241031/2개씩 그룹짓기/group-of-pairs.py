n = int(input())

lst = list(map(int,input().split()))
lst.sort()
result = []
for i in range(len(lst)):
    line = []
    line.append(lst[i])
    line.append(lst[-(i+1)])
    line.sort()
    if line not in result : 
        result.append(line)
max = 0 
for i in result:
    sum =0 
    for k in range(len(i)):
        sum += i[k]
        if max <= sum :
            max = sum
print(max)