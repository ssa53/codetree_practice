dirs = list(str(input()))
x,y=0,0
dir_num = 3 
dx,dy=[1,0,-1,0],[0,-1,0,1]

for i in dirs:
    if i == 'R': 
        dir_num = (dir_num + 1) % 4 
    elif i == 'L':
        dir_num = (abs(dir_num - 1)) % 4
    else:
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x,y)
        
     
