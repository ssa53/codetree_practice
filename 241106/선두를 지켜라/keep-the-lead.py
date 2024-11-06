MAX = 1000000
n,m=tuple(map(int,input().split()))
arr_a,arr_b = [0]*(MAX+1),[0]*(MAX+1)
time_a = 1
for i in range(n):
    v,t=tuple(map(int,input().split()))
    for j in range(t):
        arr_a[time_a] = arr_a[time_a - 1] + v
        time_a += 1

time_b = 1
for i in range(n):
    v,t=tuple(map(int,input().split()))
    for j in range(t):
        arr_b[time_b] = arr_b[time_b - 1] + v
        time_b += 1

leader,ans = 0,0
for i in range(1,time_a):
    if arr_a[i] > arr_b[i]:
        if leader == 2:
            ans += 1
        leader = 1

    elif arr_a[i]<arr_b[i]:
        if leader == 1:
            ans += 1 
        
        leader = 2

print(ans)