n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if i<=j and j<=k and a[i]<=a[j] and a[j]<=a[k]:
                cnt += 1 

print(cnt)