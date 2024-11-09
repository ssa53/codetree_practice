#n은 개발자 수 k는 감염가능한 횟수 p는 처음 감염된 개발자의 idx T는 반복횟수 
#t는 시각,x,y는 악수하는 사람idx 
n,k,p,T=map(int,input().split())
people = [0]*(n)
people[p-1] = 1
lst = []
for i in range(T):
    t,x,y= map(int,input().split())
    lst.append([t,x,y])

lst.sort(key=lambda x: x[0])

for i in range(k):
    if lst[i][1] == p :
        people[lst[i][2]-1] = 1
    elif lst[i][2] == p :
        people[lst[i][1]-1] = 1
    else:
        pass

for i in people:
    print(i,end="")