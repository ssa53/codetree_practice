n,k = map(int,input().split())

lst = list(map(int,input().split()) )
lst.sort()
for i in range(len(lst)):
    if i == k-1:
        print(lst[i])