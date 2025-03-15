class Student:
    def __init__(self,name,a,b,c):
        self.name,self.a,self.b,self.c=name,a,b,c
    
n=int(input())
students = []
for i in range(n):
    name,a,b,c=tuple(input().split())
    students.append(Student(name,int(a),int(b),int(c)))
    
students.sort(key=lambda x:x.a+x.b+x.c)

for student in students:
    print(student.name, student.a,student.b,student.c)
    