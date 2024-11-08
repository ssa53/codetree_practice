dir = 0
x,y = 0,0
dx,dy=[0,1,0,-1],[1,0,-1,0]
sentence = list(str(input()))
for i in sentence : 
    if i == 'L':
        dir = (dir-1) % 4 
    elif i == 'R':
        dir = (dir+1) % 4 
    elif i == 'F':
        if dir == 0:
            x = x + dx[0]
            y = y + dy[0]
        elif dir == 1:
            x = x + dx[1]
            y = y + dy[1]            
        elif dir == 2:
            x = x + dx[2]
            y = y + dy[2]            
        elif dir == 3:
            x = x + dx[3]
            y = y + dy[3]            

print(x,y)