lst = list(map(int,input().split()))
n = len(lst)
rst = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            rst.append(abs(sum(lst)-2*(lst[i]+lst[j]+lst[k])))
print(min(rst))


