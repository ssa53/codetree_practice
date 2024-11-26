n,m=map(int,input().split())
arr = [
    [0]*n
    for i in range(n)
]
dxs = [0, 1,  0, -1]
dys = [1, 0, -1,  0]
def count(r,c):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    
    return cnt 
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m
    
for i in range(m):
    r,c=map(int,input().split())
    arr[r-1][c-1] = 1 
    if count(r-1,c-1) == 3:
        print(1)
    else:
        print(0)
