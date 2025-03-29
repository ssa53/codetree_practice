import sys
int_min = sys.maxsize 
n = int(input())
A = list(map(int, input().split()))

min = int_min 
for i in range(n):
    sum=0
    for j in range(n):
        if j!=i:
            sum+=abs(j-i)*A[j] 
    if sum<min:
        min=sum
print(min)
            