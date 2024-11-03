num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1,d1,m2,d2 = map(int,input().split())
a = str(input())

lst = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

def get_day(month,day):
    sum=0
    for i in range(1,month):
        sum+= num_of_days[i]
    sum += day
    return sum 

result_day = get_day(m2,d2)-get_day(m1,d2)

result = result_day // 7 


if result_day % 7  >= lst.index(a)+1:
    result +=1 

print(result)