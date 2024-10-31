n,k = map(int,input().split())

lst = list(map(int,input().split()) )
for i in range(len(lst)):
    if i ==  k:
        print(lst[i])
        break