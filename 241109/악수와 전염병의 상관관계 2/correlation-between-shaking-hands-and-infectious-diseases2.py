class Shake :
    def __init__(self,time,person1,person2):
        self.time,self.person1,self.person2 = time,person1,person2
    
n,k,p,t = map(int,input().split())
shakes = []
for i in range(t):
    time,person1,person2 = map(int,input().split())
    shakes.append(Shake(time,person1,person2))

shake_num = [0] * (n+1)
infected = [False] * (n+1)

infected[p] = True

shakes.sort(key = lambda x : x.time)

for shake in shakes:
    target1 = shake.person1
    target2 = shake.person2
    if infected[target1]:
	    shake_num[target1] += 1
    if infected[target2]:
		shake_num[target2] += 1
	
	# target1이 감염되어 있고 아직 K번 이하로 악수했다면 target2를 전염시킵니다.
	if shake_num[target1] <= k and infected[target1]:
		infected[target2] = True
	
	# target2가 감염되어 있고 아직 K번 이하로 악수했다면 target1을 전염시킵니다.
	if shake_num[target2] <= k and infected[target2]:
		infected[target1] = True

for i in range(1,n+1):
    if infected[i]:
        print(1,end="")
    else:
        print(0,end="")