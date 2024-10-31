a = list(str(input()))
b = list(str(input()))



a.sort()
b.sort()
result = True 
if len(a) != len(b):
    result = False
for i in range(len(a)):
    if a[i]==b[i]:
        pass
    else:
        result = False 
        break
        

if result == True:
    print("Yes")
else:
    print("No")