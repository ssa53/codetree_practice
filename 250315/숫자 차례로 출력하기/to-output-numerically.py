n = int(input())

def sol(n):
    if n==0:
        return
    print(n,end=" ")
    sol(n-1)

def rev_sol(n):
    if n==0:
        return 
    rev_sol(n-1)
    print(n,end=" ")

rev_sol(n)
print()
sol(n)