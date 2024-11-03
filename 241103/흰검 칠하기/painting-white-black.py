MAX = 100000

n= int(input())
lst = [0] * 200001
cnt_black = [0] * 200001
cnt_white = [0] * 200001
black,white,gray = 0,0,0

cur = MAX
for i in range(n):
	dist, dir = input().split()
	dist = int(dist)
	if dir == "L":
		while dist>0:
			lst[cur] = 1 
			cnt_white[cur] += 1
			dist -= 1

			if dist:
				cur -= 1 
	else:
		while dist>0:
			lst[cur] = 2
			cnt_black += 1
			dist -= 1
			
			if dist:
				cur+=1

for i in range(200001):
	if cnt_black[i]>=2 and cnt_white[i] >=2:
		gray += 1
	elif lst[i] == 1:
		white += 1
	elif lst[i] == 2:
		black += 1
			

print(white,black,gray)