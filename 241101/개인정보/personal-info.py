class my:
    def __init__(self,name,h,m):
        self.name=name
        self.h=h
        self.m=m

people=[]

for i in range(5):
    name,h,m=input().split()
    people.append(my(str(name),int(h),float(m)))
    
people.sort(key=lambda x:(x.name))
print("name")
for i in people:
    print(i.name,i.h,i.m)

print("")
people.sort(key=lambda x: -x.h)
print("height")
for i in people:
    print(i.name,i.h,i.m)