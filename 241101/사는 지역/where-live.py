class my:
    def __init__(self,name,addr,loc) :
        self.name=name
        self.addr=addr
        self.loc=loc

n = int(input())
people = []
for i in range(n):
    name,addr,loc=tuple(input().split())
    person = my(name,addr,loc)
    people.append(person)
    
name_lst =[]
for i in range(n):
    name_lst.append(people[i].name)

name_lst.sort()
for i in range(n):
    if name_lst[-1] == people[i].name:
        print("name",people[i].name)
        print("addr",people[i].addr)
        print("city",people[i].loc)