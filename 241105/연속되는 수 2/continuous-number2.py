n = int(input())
lst = []
cnt_lst = []

for i in range(n):
    num = int(input())
    lst.append(num)
ans,cnt = 0,0
for i in range(n):
    if i>=1 and lst[i] == lst[i-1]:
        cnt +=1 
    else:
        cnt = 1 

    ans = max(ans,cnt)

print(ans)