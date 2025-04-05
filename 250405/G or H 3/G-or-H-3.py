n,k=map(int,input().split())
arr = ['']*10001

for i in range(n):
    x,y=input().split()
    x=int(x)
    y=str(y)
    arr[x] = y
    
ans = 0
for i in range(len(arr)-k):
    maxi = 0
    for j in range(i,i+k+1):
        if arr[j] == 'G':
            maxi += 1
        elif arr[j] == 'H':
            maxi += 2
    ans = max(maxi,ans)
print(ans)