n = int(input())
lst = []
cnt_lst = []

for i in range(n):
    num = int(input())
    lst.append(num)
cnt = 1
for i in range(n):
    if i == 0 :
        pass
    elif lst[i] == lst[i-1] :
        cnt +=1 
    elif lst[i] != lst[i-1 ] : 
        cnt_lst.append(cnt)
        cnt = 1 
if cnt_lst ==[]:
    print(1)
else:
    print(max(cnt_lst))