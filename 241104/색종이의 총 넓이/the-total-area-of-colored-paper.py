n = int(input())
lst_rect = [
    tuple(map(int,input().split()))
    for i in range(n)
]
    
MAX = 200
OFFSET = 100

lst = [
    [0]*(MAX+1)
    for i in range(MAX+1)
]

for x,y in lst_rect :
    x,y = x+OFFSET , y+OFFSET
    for i in range(x,x+8):
        for j in range(y,y+8):
            lst[i][j] = 1

area = 0
for i in range(0,MAX+1):
    for j in range(0,MAX+1):
        if lst[i][j]==1:
            area += 1
        
print(area)