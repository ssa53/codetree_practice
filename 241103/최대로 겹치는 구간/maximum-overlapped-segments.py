n = int(input())
lst = [
    0 for i in range(200)
]
for i in range(n):
    a,b=map(int,input().split())
    for j in range(a+100,b+101):
        lst[j] +=1

print(max(lst))