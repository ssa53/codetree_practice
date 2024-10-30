n = int(input())
lst = list(map(int,input().split()))

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a*b)// gcd(a,b)

result = lst[0]

for i in range(len(lst)-1):
    result = lcm(result,lst[i+1])

print(result)