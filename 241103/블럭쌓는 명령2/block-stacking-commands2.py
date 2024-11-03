n,k=map(int,input().split())

lst = [
    0 for i in range(n):
]

for i in range(k):
    a,b = map(int,input().split())
    lst[a,b+1] += 1

max= 0
for i in lst:
    if i >= max:
        max = i

print(max)