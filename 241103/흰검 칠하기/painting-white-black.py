n = int(input())
OFFSET = 100000
MAX = 200000
segment = []
start = 0
for i in range(n):
    distance,direction = input().split()
    distance = int(distance)
    if direction == "L":
        left = start - distance
		right = start
		start = start - distance
		segment.append([left,right])
	else:
		left = start 
		right = start + distance
		start = start + distance
		segment.append([left,right])
checked = [[0,"color"]] * (MAX+1)
for x,y in segment:
	x,y = x+OFFSET,y+OFFSET
	if y > x : 
		for i in range(x,y):
			checked[i][0] += 1000
			checked[i][1] = "black"
	elif y < x: 
		for i in range(y,x,-1):
			checked[i][0] += 1
			checked[i][1] = "white"
white = 0
gray = 0
black = 0	
for i in checked:
	if i//1000 >= 2 and i%1000 >= 2:
		gray += 1
	else: 
		if i[1] == "black":
			black += 1
		elif i[1] == "white":
			white += 1 

print(white,black,gray)