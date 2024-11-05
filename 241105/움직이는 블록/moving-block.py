n = int(input())
lst = []
for i in range(n):
    data = int(input())
    lst.append(data)

avg = int(sum(lst)/n)

def make_same(lst,avg):
    sum = 0 
    for i in range(len(lst)):
        sum += lst[i] - avg 
    return int(sum)
    
print(make_sum(lst,avg))