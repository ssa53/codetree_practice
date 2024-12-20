n,s=map(int,input().split())
lst = list(map(int,input().split()))
sum_lst = []
for i in range(len(lst)):
    sum = 0 
    for j in range(i+1,len(lst)):
        sum += lst[i]+lst[j]
    sum -= s 
    sum_lst.append(sum)
for i in range(len(sum_lst)):
    if sum_lst[i] < 0:
        sum_lst[i] = -sum_lst[i]
print(min(sum_lst))
        
        
        