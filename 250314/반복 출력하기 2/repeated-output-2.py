n = int(input())

def sol(n):
    if n==1:
        print("HelloWorld")
    else:
        sol(n-1)
        print("HelloWorld")

sol(n)