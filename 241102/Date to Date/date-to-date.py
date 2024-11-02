num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1,d1,m2,d2 = map(int,input().split())

def get_days(month,day):
    sum = 0
    for i in range(len(num_of_days)):
        if month != i:
            sum += num_of_days[i]
        if month == i:
            sum += day
            break
    return sum
            
start = get_days(m1,d1)
end = get_days(m2,d2)

print(end-start+1)