n = int(input())

class student:
    def __init__(self,h,m,idx):
        self.h=h
        self.m=m
        self.idx=idx

lst = []
for i in range(n):
    h,m=map(int,input().split())
    idx=i+1
    lst.append(student(h,m,idx))

# h 오름차순
# if h same m 내림차순

lst.sort(key=lambda x:(x.h,-x.m))

for i in lst:
    print(i.h,i.m,i.idx)