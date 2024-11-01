n = int(input())

class Student:
    def __init__(self,h,m,num):
        self.h=h
        self.m=m
        self.num=num

students = []
for i in range(n):
    h,m= map(int,input().split())
    students.append(Student(h,m,i+1))

students.sort(key=lambda x: (-x.h,-x.m,x.num))
for i in students:
    print(i.h,i.m,i.num)