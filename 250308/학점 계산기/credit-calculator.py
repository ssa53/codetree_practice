n=int(input())
lst = list(map(float,input().split()))
print(f'{sum(lst)/n:0.1f}')
if sum(lst)/n >= 4.0:
    print("Perfect")
elif sum(lst)/n >=3.0:
    print("Good")
else:
    print("Poor")
