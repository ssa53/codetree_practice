n = int(input())
lst = list(map(int,input().split()))
mx = 0
for i in range(n):
    for j in range(i+2,n):
        sum = 0
        sum += lst[i]+lst[j]
        mx=max(mx,sum)
print(mx)
            
        