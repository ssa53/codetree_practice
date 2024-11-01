class my:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

n = int(input())
people = [] 
for i in range(n):
    name,height,weight = tuple(input().split())
    people.append(my(name,height,weight))
    
people.sort(key=lambda x: x.height)

for i in people:
    print(i.name,i.height,i.weight)