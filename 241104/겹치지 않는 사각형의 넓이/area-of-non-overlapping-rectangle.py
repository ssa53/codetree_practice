OFFSET = 1000
MAX = 2000
x1a,y1a,x2a,y2a = map(int,input().split())
x1b,y1b,x2b,y2b = map(int,input().split())
x1m,y1m,x2m,y2m = map(int,input().split())

checked = [
    [0]*(MAX+1)
    for i in range(MAX+1)
]


x1a,y1a=x1a+OFFSET,y1a+OFFSET
x2a,y2a=x2a+OFFSET,y2a+OFFSET
for x in range(x1a,x2a):
    for y in range(y1a,y2a):
        checked[x][y] = 1

x1b,y1b=x1b+OFFSET,y1b+OFFSET
x2b,y2b=x2b+OFFSET,y2b+OFFSET
for x in range(x1b,x2b):
    for y in range(y1b,y2b):
        checked[x][y] = 2

x1m,y1m=x1m+OFFSET,y1m+OFFSET
x2m,y2m=x2m+OFFSET,y2m+OFFSET
for x in range(x1m,x2m):
    for y in range(y1m,y2m):
        checked[x][y] = 3
area = 0
for i in range(MAX+1):
    for j in range(MAX+1):
        if checked[i][j] == 1 or checked[i][j] == 2:
            area += 1

print(area)