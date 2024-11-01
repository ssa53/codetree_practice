c,m,t = input().split()
c=str(c)
m=str(m)
t=int(t)

class secrete_code:
    def __init__(self,c,m,t):
        self.c=c
        self.m=m
        self.t=t

result = secrete_code(c,m,t)
print("secret code :",result.c)
print("meeting point :",result.m)
print("time :",t)