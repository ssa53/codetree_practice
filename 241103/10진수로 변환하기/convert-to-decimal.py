binary = []
n = str(input())
for i in range(len(n)):
    binary.append(n[i])
sum=0
for i in range(len(binary)):
    sum += binary[i]*pow(2,len(binary)-1-i)
    
print(sum)