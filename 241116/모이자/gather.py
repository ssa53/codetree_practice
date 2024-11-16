import sys
n = int(input())
lst = list(map(int,input().split()))
result = []
# lst 에는 lst[0] = 1 0번지에 1명이 산다. 
for i in range(len(lst)):
    sum=0
    for j in range(len(lst)):
        distance = j-i
        if j-i <0 : 
            distance = i-j
        sum += distance * (lst[j]) 

    result.append(sum)
print(min(result))


            
        
        
        
