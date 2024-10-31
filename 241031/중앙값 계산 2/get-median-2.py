n = int(input())
_input = list(map(int,input().split()))
lst = []
for i in range(n):
    a = _input[i]
    lst.append(a)
    lst.sort()
    if (i+1)%2 != 0:
        print(lst[len(lst)//2])