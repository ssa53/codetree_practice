n = int(input())

def sol(n):
    if n<10:
        return pow(n,2)
    return sol(n//10) + pow((n%10),2)

print(sol(n))