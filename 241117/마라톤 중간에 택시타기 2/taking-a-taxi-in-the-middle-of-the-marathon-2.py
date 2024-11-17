n = int(input())
lst = [
    list(map(int,input().split()))
    for _ in range(n)
]
result = []
for i in range(1,n-1):
    sum = 0
    lst_copy = lst.copy()
    del lst_copy[i]
    for j in range(n-2):
        diff = abs(lst_copy[j+1][0]-lst_copy[j][0])+abs(lst_copy[j+1][1]-lst_copy[j][1])
        sum += diff 
    result.append(sum)
print(min(result))
