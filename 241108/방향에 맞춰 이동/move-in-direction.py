x,y = 0,0
dx,dy = [-1,0,0,1],[0,-1,1,0]
n = int(input())
for i in range(n):
    dir,dis = input().split()
    dis = int(dis)
    if dir == 'W':
        x += dx[0] * dis
        y += dy[0] * dis
    elif dir == 'S':
        x += dx[1] * dis 
        y += dy[1] * dis
    elif dir == 'N':
        x += dx[2] * dis
        y += dy[2] * dis
    elif dir == 'E':
        x += dx[3] * dis 
        y += dy[3] * dis

print(x,y)