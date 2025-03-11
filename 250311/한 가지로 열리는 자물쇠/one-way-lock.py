N = int(input())
a, b, c = map(int, input().split())

def get_nums(n,a):
    nums = 0
    for i in range(1,n+1):
        if abs(i-a)>2 : 
            nums += 1 
    return nums 

result = pow(N,3) - get_nums(N,a)*get_nums(N,b)*get_nums(N,c)
print(result)