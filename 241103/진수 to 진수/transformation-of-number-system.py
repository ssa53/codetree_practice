a,b = map(int,input().split())
n = str(input())
lst = []
for i in range(len(n)):
    lst.append(int(lst[i]))
sum=0
for i in range(len(n)):
    sum += lst[i]*pow(a,len(n)-1-i):
result=[]
while True:
    if sum<b:
        result.append(sum)
        break
    result.append(sum%b)
    sum //= b

for i in result:
    print(i,end="")