lst = list(str(input()))
x,y=0,0
dir=3
dxs,dys = [1,0,-1,0],[0,-1,0,1]
time = 0
for i in range(len(lst)):
    if lst[i] == 'F':
        x,y=x+dxs[dir],y+dys[dir]
        time += 1 
    elif lst[i] == 'L':
        dir = (dir-1)%4
        time += 1 
    elif lst[i] == 'R':
        dir = (dir+1)%4
        time += 1
    if x==0 and y==0:
        break
if x==0 and y==0:
    print(time)
else:
    print(-1)
    