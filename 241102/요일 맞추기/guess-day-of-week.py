num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def get_day(month,day):
    sum=0
    for i in range(1,month):
        sum+= num_of_days[i]
    sum += day
    return sum 
lst = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
m1,d1,m2,d2 = map(int,input().split())
result = get_day(m2,d2) - get_day(m1,d1)
while result <0:
    result += 7
x=result%7
print(lst[x])