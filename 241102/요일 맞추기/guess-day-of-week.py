num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def get_day(month,day):
    sum=0
    comp = 0
    while comp != month - 1:
        sum += num_of_days[comp]
        comp +=1
    sum += day
    return sum 
lst = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
m1,d1,m2,d2 = map(int,input().split())
result = get_day(m2,d2) - get_day(m1,d1)

x=result%7
print(lst[x])