def get_min(h,m):
    return (h-1)*60 + m ;

a,b,c,d= map(int,input().split())
print(get_min(c,d)-get_min(a,b))