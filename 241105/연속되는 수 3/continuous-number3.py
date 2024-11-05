n = int(input())
lst = [
    int(input())
    for i in range(n)
]
#부호 (lst[i]<0 or lst[i]>0) 이 같은거중에 길이(cnt)가 제일 큰거..
ans,cnt =0, 0
for i in range(n):
    if i>=1 and lst[i]*lst[i-1] < 0 :
        cnt += 1
    else:
        cnt = 1 
    ans = max(ans,cnt)

print(ans)