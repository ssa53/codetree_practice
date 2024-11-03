n=int(input())
lst = [
    0 for i in range(2001)
]
start = 1000
for i in range(n):
    num,direct = input().split()
    num = int(num)
    if direct == "R":
        for j in range(start,start+num+1):
            lst[j] += 1
            start = start+num 
    elif direct == "L":
        for j in range(start+num,start-1,-1):
            lst[j] += 1 
            start = start+num
sum = 0 
for j in range(len(lst)):
    if lst[j] == max(lst):
        sum += 1 

print(sum)