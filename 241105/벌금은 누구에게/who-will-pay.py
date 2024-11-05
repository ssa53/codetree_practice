n,m,k=map(int,input().split())
lst_student = [
    0 
    for i in range(101)
]
#lst_student = [ 0 0 0 0 0 0 0 0 0 0 0 0 0 0........ ]
for i in range(n):
    idx = int(input())
    lst_student[idx] += 1 
    for j in range(len(lst)):
        if lst[j] == m:
            print(j)