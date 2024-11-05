n,t = map(int,input().split())
lst = list(map(int,input().split()))
# t==3 이면 index 0, 1 은 불가능 .....
# t==2 이면 index 0은 불가능 ...
# i <= t-2 이면 불가능....
ans,cnt = 0,0
for i in range(n):
    if i>= 1 and lst[i] > t :
        cnt += 1 
    else :
        cnt = 1 
    ans = max(cnt-1,ans)

print(ans)