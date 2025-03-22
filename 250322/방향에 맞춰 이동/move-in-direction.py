n = int(input())
x,y=0,0
dx,dy=[1,0,-1,0],[0,-1,0,1]
for i in range(n):
    d,l = tuple(input().split())
    l=int(l) 
    if d=='E':
        x = x + dx[0]*l
        y = y + dy[0]*l
    elif d=='S':
        x = x + dx[1]*l
        y = y + dy[1]*l
    elif d=='W':
        x = x + dx[2]*l
        y = y + dy[2]*l
    else:
        x = x + dx[3]*l
        y = y + dy[3]*l
         
print (x,y)