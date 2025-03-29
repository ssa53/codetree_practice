n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

mapper={
    'R':0,
    'D':1,
    'U':2,
    'L':3
}

dxs,dys=[0,1,-1,0],[1,0,0,-1]
r,c,move_dir = r-1,c-1,mapper[d]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

for _ in range(t):
    nx,ny=x+dxs[move_dir],y+dys[move_dir]
    if in_range(nx,ny):
        x,y=nx,ny
    else:
        move_dir = 3-move_dir

print(x+1,y+1)