abilities = list(map(int, input().split()))

# Please write your code here.
min = sum(abilities) 
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            if sum(abilities) - 2*(abilities[i]+abilities[j]+abilities[k]) <= min:
                min = sum(abilities) - 2*(abilities[i]+abilities[j]+abilities[k])
print(min)