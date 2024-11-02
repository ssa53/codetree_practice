a,b,c = map(int,input().split())
if a <= 11 and b <=11 and c < 11:
    print(-1)

def get_min(day,hour,minute):
    return (day-1)*24*60 + hour*60 + minute

start = get_min(11,11,11)
end = get_min(a,b,c)

print(end-start)