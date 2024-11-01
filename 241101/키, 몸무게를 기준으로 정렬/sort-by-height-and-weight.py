class my:
    def __init__(self,name,h,m):
        self.name=name
        self.h=h
        self.m=m
n = int(input())
people = []
for i in range(n):
    name,h,m=input().split()
    people.append(my(str(name),int(h),int(m)))
    
people.sort(key=lambda x:(x.h,-x.m))

for person in people:
    print(person.name,person.h,person.m)