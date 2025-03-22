N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)] 

arr = [0]*(n+1)
ans = []
for i in student:
    arr[i] += 1 
    for j in range(len(arr)):
        if arr[j] >= k:
            ans.append(j)
            
if len(ans) != 0 :
    print(ans[0])
else:
    print(-1)

# Please write your code here.