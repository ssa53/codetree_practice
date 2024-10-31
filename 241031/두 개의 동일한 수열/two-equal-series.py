n = int(input())
lst_a = list(map(int,input().split()))
lst_b = list(map(int,input().split()))
lst_a.sort()
lst_b.sort()
result = True
for i in range(len(lst_a)):
    if lst_a[i] != lst_b[i]:
        result = False
    else: 
        pass

if result == True:
    print("Yes")
else:
    print("No")