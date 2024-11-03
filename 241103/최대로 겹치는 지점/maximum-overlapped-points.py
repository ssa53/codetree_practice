n = int(input())
lst = [
    0 for i in range(100+1)
]
for i in range(n):
    x1,x2=map(int,input().split())
    for j in range(x1,x2+1):
        lst[j] += 1

print(max(lst))