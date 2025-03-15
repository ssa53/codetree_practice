n = int(input())

def sol(n):
    if n==0:
        return
    print(n,end=" ")
    sol(n-1)

def rev_sol(n):
    if n==0:
        return 
    print(n,end=" ")
    rev_sol(n-1)

rev_sol(n)
sol(n)