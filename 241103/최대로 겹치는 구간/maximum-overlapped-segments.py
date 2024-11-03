n = int(input())
lst = [
    0 for i in range(200)
]
for i in range(n):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        lst[j] +=1

print(max(lst))