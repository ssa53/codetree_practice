n,k=map(int,input().split())
lst = list(map(int,input().split()))
sum_lst = []
for i in range(n-k+1):
    sum = 0
    sum += lst[i]
    sum_lst.append(sum)
print(max(sum_lst))

