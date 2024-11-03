a,b = map(int,input().split())
n = str(input())
lst = []
for i in range(len(n)):
    lst.append(int(n[i]))
sum=0
for i in range(len(lst)):
    sum += lst[i]*pow(a,len(lst)-1-i)
result=[]
while True:
    if sum<b:
        result.append(sum)
        break
    result.append(sum%b)
    sum //= b

for i in result:
    print(i,end="")