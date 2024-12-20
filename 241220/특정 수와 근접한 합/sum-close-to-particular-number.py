n,s=map(int,input().split())
lst = list(map(int,input().split()))
sum_lst = []
SUM = 0
for k in lst:
    SUM += k
for i in range(len(lst)-1):
    sum = 0 
    for j in range(i+1,len(lst)):
        sum = lst[i]+lst[j]
        sum_lst.append(SUM-sum-s)

print(min(sum_lst))
        
        
        