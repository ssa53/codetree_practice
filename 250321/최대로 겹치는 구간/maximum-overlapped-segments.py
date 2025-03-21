OFFSET = 100
MAX_R = 200

n = int(input())
segments = [
    map(int,input().split())
    for i in range(n)
]
arr = [0] * (MAX_R+1)

for x1,x2 in segments:
    x1,x2 = x1+OFFSET,x2+OFFSET
    for i in range(x1,x2):
        arr[i] += 1 

print(max(arr))