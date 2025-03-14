y = int(input())

# Please write your code here.
def is_yun(n):
    if n%4==0 and (n%100==0 and n%400 != 0) :
        return True 
    else:
        return False 

if is_yun(y) == True : 
    print("true")
else:
    print("false")