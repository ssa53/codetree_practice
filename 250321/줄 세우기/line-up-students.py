class Student:
    def __init__(self,height,weight,number):
        self.height,self.weight,self.number = height,weight,number

n = int(input())
students = []
for i in ragne(1,n+1):
    height,weight = tuple(map(int,input().split()))
    students.append(Student(height,weight,i))
    

students.sort(key=lambda x:(-x.height,-x.weight,x.number))

for student in students:
    print(student.height,student.weight,student.number) 
    
