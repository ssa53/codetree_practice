x1a,y1a,x2a,y2a = map(int,input().split())
x1b,y1b,x2b,y2b = map(int,input().split())
OFFSET = 1000
MAX = 2000
#a의 좌표를 1로 설정하고... b이면 0으로 초기화....1로돼있는 x좌표 최대-최소
#y좌표 최대 - 최소 구해서 곱하면 넓이가 됌.
#좌표 만들었어.
checked = [
    [0]*(MAX+1)
    for i in range(MAX+1)
]
#a의 좌표 1로 설정..
x1a,y1a,x2a,y2a = x1a+OFFSET,y1a+OFFSET,x2a+OFFSET,y2a+OFFSET
for i in range(x1a,x2a):
    for j in range(y1a,y2a):
        checked[i][j] = 1

#b의 좌표 0으로 대입.
x1b,y1b,x2b,y2b=x1b+OFFSET,y1b+OFFSET,x2b+OFFSET,y2b+OFFSET
for i in range(x1b,x2b):
    for j in range(y1b,y2b):
        checked[i][j] = 0

garo_lst=[]
sero_lst=[]
for i in range(MAX+1):
    for j in range(MAX+1):
        if checked[i][j]==1:
            garo_lst.append(i-OFFSET)
            sero_lst.append(j-OFFSET)
if garo_lst == [] or sero_lst == [] :
    print(0)
garo = max(garo_lst)-min(garo_lst)+1
sero = max(sero_lst)-min(sero_lst)+1
print(sero * garo)