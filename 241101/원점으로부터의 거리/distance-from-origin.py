class dots:
    def __init__(self,a,b,num):
        self.a=a
        self.b=b
        self.num=num

n=int(input())
lst = []
for i in range(n):
    a,b=map(int,input().split())
    lst.append(dots(a,b,int(i+1)))
    
lst.sort(key=lambda x:(abs(x.a)+abs(x.b) ,x.num ))

for i in lst:
    print(i.num)