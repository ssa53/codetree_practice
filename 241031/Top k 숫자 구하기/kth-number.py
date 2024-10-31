n,k = map(int,input().split())

lst = list(map(int,input().split()) )
for i in range(len(lst)):
    if k > len(lst):
        break
    if i ==  k:
        print(lst[i])