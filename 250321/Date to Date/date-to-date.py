def get_days(m,d):
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days=1
    for i in range(1,m):
        days += num_of_days[i]
    days += d
    return days 

a,b,c,d=map(int,input().split())
print(get_days(c,d)-get_days(a,b))
        