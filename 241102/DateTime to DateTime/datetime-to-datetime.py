a,b,c = map(int,input().split())

def get_min(day,hour,minute):
    return (day-1)*24*60 + hour*60 + minute

start = get_min(11,11,11)
end = get_min(a,b,c)

if end-start >= 0:
    print(end-start)
else:
    print(-1)