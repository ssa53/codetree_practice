n = int(input())
lst = list(map(int,str(n)))
def change01(num):
    if num == 1:
        return 0
    elif num == 0:
        return 1 
mx = 0
for i in range(len(lst)):
    sum=0
    lst_copy = lst.copy()
    lst_copy[i] = change01(lst_copy[i]) 
    for j in range(len(lst)):
        sum += lst_copy[j]*(len(lst)-(j+1))
        print(sum)
    mx = max(mx,sum)
        
print(mx)
        
    