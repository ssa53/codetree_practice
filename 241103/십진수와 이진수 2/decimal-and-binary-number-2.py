n = str(input())
lst = []
for i in range(len(n)):
    lst.append(n[i])
sum = 0
for i in range(len(lst)):
    sum += lst[i]*pow(2,len(lst)-1-i) 
    
sum *= 17

    
result = []
    
while True:
    if sum < 2:
        result.append(n)
        break
        
    result.append(sum%2)
    sum//=2
    
for i in result[::-1]:
    print(i,end="")