a, b = map(int, input().split())

def is_3x(n):
    if n%3==0:
        return True
    else:
        return False 

def is_369_in(n):
    if '3' in list(str(n)) or '6' in list(str(n)) or '9' in list(str(n)):
        return True
    else:
        return False 
rst = 0
for i in range(a,b+1):
    if is_3x(i) == True or is_369_in(i)==True :
        rst+=1
print(rst)
        
    
    
    