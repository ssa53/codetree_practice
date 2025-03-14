y = int(input())

# Please write your code here.
def is_yun(y):
    if y%4!=0 :
        return False
    if y%100 == 0 and y%400 != 0 :
        return False 
    return True 

print("true") if is_yun(y):
else: print("false")
