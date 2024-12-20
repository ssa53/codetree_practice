n,s=map(int,input().split())
lst = list(map(int,input().split()))
sum_lst = []
for i in range(len(lst)):
    sum = 0 
    for j in range(i+1,len(lst)):
        sum += lst[i]+lst[j]
    sum -= s 
    sum_lst.append(sum)
print(min(sum_lst))

        
        
        