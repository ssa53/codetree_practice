n,m,k=map(int,input().split())
lst_student = [
    0 
    for i in range(101)
]
penalized_person = [
    int(input())
    for i in range(m)
]
#lst_student = [ 0 0 0 0 0 0 0 0 0 0 0 0 0 0........ ]
ans = 0
for target in penalized_person:
    lst_student[target] += 1 
    
    if lst_student[target]>=k:
        ans = target 
        break 

print(ans)