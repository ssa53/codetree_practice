n, m = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

cnt = 0 
for i in range(0,n-m+1):
    if sorted(arr1[i:i+m])==sorted(arr2):
        cnt += 1 
print(cnt) 