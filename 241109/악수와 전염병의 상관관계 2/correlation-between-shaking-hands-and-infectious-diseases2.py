#n은 개발자 수 k는 감염가능한 횟수 p는 처음 감염된 개발자의 idx T는 반복횟수 
#t는 시각,x,y는 악수하는 사람idx 
n,k,p,T=map(int,input().split())
people = [0]*(n)
people[p] = 1
time = []
lst = []
for i in range(T):
    t,x,y= map(int,input().split())
    time.append(t)
    lst.append([x,y])

time.sort()
for i in range(k):
    for j in range(2):
        if lst[i][0] == p:
            people[lst[i][1]] = 1 
        elif lst[i][1] == p :
            people[lst[i][0]] = 1 
        else: 
            pass

for i in people:
    print(i,end="")