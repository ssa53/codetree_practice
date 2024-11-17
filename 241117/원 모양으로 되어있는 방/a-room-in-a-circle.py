n = int(input())
lst = [
    int(input()) 
    for i in range(n)
]
sum_lst = []
for i in range(n):
    sum = 0
    for j in range(n):
        diff = j-i
        if j-i < 0:
            diff = 5-abs(j-i)
        dist = lst[j]*diff
        sum += dist
    sum_lst.append(sum)
print(min(sum_lst))
 


    