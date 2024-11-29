n,k=map(int,input().split())
lst = list(map(int,input().split()))
mx=0
for i in range(n-k+1):
    sum = 0  
    for j in range(i,i+3):
        sum += lst[j] 
    mx = max(sum,mx)

print(mx)
