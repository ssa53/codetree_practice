n = int(input())

def func(n):
    if n%2 == 0:
        if n == 1:
            return 0
        return func(n/2) + 1 
    elif n%2 != 0:
        if n==1:
            return 0
        return func(3*n+1) +1
        
print(func(n))