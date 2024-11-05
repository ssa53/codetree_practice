n = int(input())
OFFSET = 100
MAX = 200
#rects에 rect n개만큼 저장.
rects = []
for i in range(n):
    rect = list(map(int,input().split()))
    rects.append(rect)
#좌표생성
checked = [
    [0]*(MAX+1)
    for i in range(MAX+1)
]

#번갈아가며 red 1 blue 2로 칠해. 범위는 rects의 [i]의 [0],[1]
for i in range(n): #if i%2 == 0 red.... i%2 == 1 blue....
    if i % 2 == 0:
        for j in range(rects[i][0]+OFFSET,rects[i][2]+OFFSET):
            for k in range(rects[i][1]+OFFSET,rects[i][3]+OFFSET): 
                checked [j][k] = 1 
    elif i%2 == 1 :
        for j in range(rects[i][0]+OFFSET,rects[i][2]+OFFSET):
            for k in range(rects[i][1]+OFFSET,rects[i][3]+OFFSET): 
                checked [j][k] = 2

#좌표가 2인 좌표 개수 찾기..
ans = 0
for i in range(MAX+1):
    for j in range(MAX+1):
        if checked[i][j] == 2:
            ans += 1 

print(ans)