months = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1,d1,m2,d2=map(int,input().split())
what_yoil = str(input())
result = 0 
if m2-m1 > 1:
    result = months[m1-1]-d1 + d2 
    for i in range(m1+1,m2):
        result += months[i-1] 
elif m2-m1 == 1:
    result = months[m1-1]-d1 + d2 
elif m2==m1 : 
    result = d2-d1 

cnt = result//7 
if result % 7 != 0 :
    cnt += 1 
print(cnt)