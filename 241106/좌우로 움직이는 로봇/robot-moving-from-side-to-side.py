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
if time_a < time_b:
	for i in range(time_a, time_b):
		arr_a[i] = arr_a[i - 1]
elif time_a > time_b:
	for i in range(time_b, time_a):
	    arr_b[i] = arr_b[i - 1]
cnt = 0
for i in range(1,max(time_b,time_a)):
    if arr_a[i] == arr_b[i] :
        if arr_a[i-1] != arr_b[i-1]:
            cnt += 1
print(cnt)