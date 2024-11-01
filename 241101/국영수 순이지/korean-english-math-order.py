n = int(input())

class score:
    def __init__(self,name,kor,eng,math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math

people = []
for i in range(n):
    name,kor,eng,math = input().split()
    people.append(score(name,int(kor),int(eng),int(math)))

people.sort(key = lambda x:(-x.kor, -x.eng, -x.math))

for i in people:
    print(i.name,i.kor,i.eng,i.math)