a = list(str(input()))
cnt = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            for l in range(k+1,len(a)):
                if a[i]=='(' and a[j]=='(' and j==i+1 and a[k] ==')' and a[l]==')' and l == k+1:
                    cnt += 1 
print(cnt)
                    
                