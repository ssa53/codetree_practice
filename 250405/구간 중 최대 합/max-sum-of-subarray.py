n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n-k+1):
    maxi = 0
    for j in range(i,i+k if i+k<n else n):
        maxi += arr[j] 
    ans = max(ans,maxi)

print(ans)