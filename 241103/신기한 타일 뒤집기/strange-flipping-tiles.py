# 1(왼쪽)이면 흰색 , 2(오른쪽)이면 검은색 
MAX = 100000
n = int(input())
lst = [0] * ((2*MAX) + 1) 
cur = MAX 
seg = [] 

for i in range(n):
    dist , dir = input().split()
    dist = int(dist)
    if dir == "R" :
        while dist > 0:
            lst[cur] = 2 
            dist -= 1
            if dist:
                cur += 1
    if dir == "L":
        while dist > 0:
            lst[cur] = 1 
            dist -= 1
            if dist:
                cur -= 1
black = 0
white = 0
for i in lst:
    if i == 2:
        black += 1
    elif i == 1:
        white += 1

print(white,black)