def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs,dys = [0,1,0,-1],[1,0,-1,0]
x,y=0,0
dir_num = 0
alphabeta=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

n,m=map(int,input().split())
arr = [
    ['0']*m 
    for _ in range(n)
]

arr[x][y] = alphabeta[0]
for i in range(1,n*m+1):
    while True:
        nx,ny = x+dxs[dir_num],y+dys[dir_num]
        if in_range(nx,ny) and arr[nx][ny]=='0':
            x,y=nx,ny
            arr[x][y] = alphabeta[i%26]
            break
        else:
            dir_num = (dir_num+1)%4
            
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()
    