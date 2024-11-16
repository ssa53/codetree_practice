n = int(input())
lst = list(map(int,input().split()))
cnt = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if k>j and j>i :
                if lst[k]>=lst[j] and lst[j]>=lst[i]:
                    cnt += 1
print(cnt)