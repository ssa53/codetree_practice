a, b = map(int, input().split())

def isPRIME(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

sum=0
for i in range(a,b+1):
    if isPRIME(i) == True : 
        sum += i 

print(sum)