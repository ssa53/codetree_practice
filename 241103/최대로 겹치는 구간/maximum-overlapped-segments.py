n = int(input())
lst = [
    0 for i in range(201)
]
for i in range(n):
    a,b=map(int,input().split())
    for j in range(a+100,b+100):
        lst[j] +=1

print(max(lst))