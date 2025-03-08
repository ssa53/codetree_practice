lst=list(map(int,input().split()))
cnt = 0 
sum = 0
for i in lst:
    if i<250:
        cnt += 1 
        sum += i
    if i>= 250:
        break
result = f'{sum/cnt:0.1f}'
print(sum,result)
        