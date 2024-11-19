n = int(input())
lst = [
    int(input())
    for i in range(n)
]
def carry(a,b,c):
    result = True
    alst,blst,clst=list(str(a)),list(str(b)),list(str(c))
    for i in range(max(len(alst),len(blst),len(clst))):
        if len(alst)<max(len(alst),len(blst),len(clst)):
            alst.insert(0,'0')
        if len(blst)<max(len(alst),len(blst),len(clst)):
            blst.insert(0,'0')
        if len(clst)<max(len(alst),len(blst),len(clst)):
            clst.insert(0,'0')
    for i in range(len(alst)):
        if int(alst[i])+int(blst[i])+int(clst[i])>=10:
            result = False
            break
        elif int(alst[i])+int(blst[i])+int(clst[i])<10:
            pass
    if result == True:
        return a+b+c
result = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            result.append(carry(lst[i],lst[j],lst[k]))
print(max(result))
                
            
