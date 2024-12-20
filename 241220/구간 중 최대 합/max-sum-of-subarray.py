n,k=map(int,input().split())
lst = list(map(int,input().split()))
sum_lst = []
for i in range(n-k+1):
    sum = 0
    for j in range(i,i+k):
        sum += lst[j]
    sum_lst.append(sum)
print(max(sum_lst))

        

