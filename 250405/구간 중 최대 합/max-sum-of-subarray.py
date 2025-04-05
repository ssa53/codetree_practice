n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    maxi = 0
    for j in range(i,i+k if i+k <n else n):
        maxi += arr[j] 
    maxi = max(ans,maxi) 

print(maxi)
        