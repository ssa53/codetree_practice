a = list(str(input())) 
cnt = 0
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]=='(' and a[j] == ')':
            cnt += 1 
            
print(cnt)