def getmin(a,b,c):
    min = a
    if min >= b:
        min = b
    if min >= c:
        min = c
    return min 

a,b,c = map(int,input().split())
print(getmin(a,b,c))