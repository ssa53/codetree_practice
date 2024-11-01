class my:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather

n = int(input())
lst = []
lst_Rain = []
for i in range(n):
    date,day,weather=tuple(input().split())
    lst.append(my(date,str(day),str(weather)))

for i in range(n):
    if lst[i].weather == "Rain":
        lst_Rain.append(lst[i].date)
    
lst_Rain.sort()
for i in range(n):
    if lst_Rain[0] == lst[i].date:
        print(lst[i].date,lst[i].day,lst[i].weather)