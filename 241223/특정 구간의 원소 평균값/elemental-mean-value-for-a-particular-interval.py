n = int(input())
lst = list(map(int,input().split()))
sum = 0
for i in range(n):
    for j in range(i,n):
        sum_val = 0
        num_lst = []
        for k in range(i,j+1):

            sum_val += lst[k] 
            num_lst.append(lst[k]) 
            avg = (sum_val / (j-i+1))

        if avg in num_lst:
            sum += 1 

print(sum)