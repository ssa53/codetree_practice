#n은 a의 반복횟수 m은 b의 반복횟수
MAX = 1000000
n,m = map(int,input().split())
a_arr = [0] * (MAX+1)
b_arr = [0] * (MAX+1)
a_lst = []
b_lst = []
#a와 b의 이동 lst에 저장
for a in range(n):
    va,ta = map(int,input().split())
    a_lst.append([va,ta])
for b in range(m):
    vb,tb = map(int,input().split())
    b_lst.append([vb,tb])
# a_lst 의 요소 [a의속도,a의이동시간] 시간을 0으로 설정... 
# lst를 담으려면 몇번 반복해야하는거지? n번동안 한번 돌리고. t초동안 돌리면 되지.
atime = 0
for i in range(n):
    for j in range(a_lst[i][1]):
        if atime == 0:
            a_arr[atime] = a_lst[i][0]
        else:
            a_arr[atime] = a_arr[atime-1]+a_lst[i][0] 
        atime += 1
btime = 0
for i in range(m):
    for j in range(b_lst[i][1]):
        if btime == 0:
            b_arr[btime] = b_lst[i][0]
        else:
            b_arr[btime] = b_arr[btime-1]+b_lst[i][0] 
        btime += 1

count = []

for i in range(atime):
    if a_arr[i] > b_arr[i]:
        First = 'a'
    elif a_arr[i] < b_arr[i]:
        First = 'b'
    elif a_arr[i] == b_arr[i]:
        First = 'same'
    count.append(First)
result = 0
for i in range(len(count)):
    if count[i] != count[i-1] and i>=1 : 
        result += 1 
    elif i == 0:
        if count[0] != 'same' : 
            result += 1 
print(result)

        
