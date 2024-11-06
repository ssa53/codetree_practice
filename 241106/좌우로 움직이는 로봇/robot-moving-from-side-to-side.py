MAX = 1000000
n,m=map(int,input().split())
arr_a , arr_b = [0]*(MAX+1) , [0]*(MAX+1)
time_a = 1
for i in range(n):
    t,d = input().split()
    t = int(t)
    if d=='R':
        for j in range(t):
            arr_a[time_a] = arr_a[time_a-1] + 1
            time_a += 1
    elif d=='L':
        for j in range(t):
            arr_a[time_a] = arr_a[time_a-1] - 1
            time_a += 1

time_b = 1
for i in range(m):
    t,d = input().split()
    t = int(t)
    if d=='R':
        for j in range(t):
            arr_b[time_b] = arr_b[time_b-1] + 1
            time_b += 1
    elif d=='L':
        for j in range(t):
            arr_b[time_b] = arr_b[time_b-1] - 1
            time_b += 1
for i in range(len(arr_a)):
    if arr_a[i] == 0:
        arr_a[i] = arr_a[time_a-1]
    if arr_b[i] == 0 :
        arr_b[i] = arr_b[time_b-1]
cnt = 0
for i in range(1,max(time_b,time_a)+1):
    if arr_a[i] == arr_b[i] :
        if arr_a[i-1] != arr_b[i-1] and max(arr_a[i-1],arr_b[i-1])-min(arr_a[i-1],arr_b[i-1])==2:
            cnt += 1
print(cnt)