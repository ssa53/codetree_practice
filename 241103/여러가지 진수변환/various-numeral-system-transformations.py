n,b=map(int,input().split())

result = []
if n < b:
    result.append(n)
    
while n >= b:
    if n < b:
        result.append(n)
        break
        
    result.append(n%b)
    n//=b
    
for i in result[::-1]:
    print(i,end="")