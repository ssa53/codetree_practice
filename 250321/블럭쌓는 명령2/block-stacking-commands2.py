n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
arr = [0] * n 

for a,b in commands : 
    for i in range(a-1,b):
        arr[i] += 1 

print(max(arr))
