n,k,T = input().split()
n = int(n)
k = int(k)
T = str(T)

lst = []
for i in range(n):
    lst.append(str(input())) 

lst.sort()
result = [] 

for i in lst:
    if list(i)[0:len(T)] == list(T):
        result.append(i)
print(result[k-1])