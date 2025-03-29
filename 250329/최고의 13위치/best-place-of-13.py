n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

mx_cnt = 0
for i in range(n):
    for j in range(n-2):
        mx_cnt = max(mx_cnt,arr[i][j]+arr[i][j+1]+arr[i][j+2])
        
print(mx_cnt)
