n,k=map(int,input().split())
lst = [
    input().split()
    for _ in range(n)
]
num_lst = []
for i in range(n):
    num_lst.append(int(lst[i][0]))
arr = [0]*max(num_lst)
for i in range(n):
    if lst[i][1] == 'G':
        arr[int(lst[i][0])-1] = 1
    elif lst[i][1] == 'H':
        arr[int(lst[i][0])-1] = 2 
sum_lst = []
print(arr)
for i in range(len(arr)-k+1):
    sum = 0
    for j in range(i,i+k+1):
        sum += arr[j]
    sum_lst.append(sum)
print(max(sum_lst))