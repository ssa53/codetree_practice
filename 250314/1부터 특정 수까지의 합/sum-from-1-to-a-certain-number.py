def getsum(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum//10

n = int(input())

print(getsum(n))