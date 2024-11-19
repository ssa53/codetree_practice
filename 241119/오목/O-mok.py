arr = [
    list(map(int,input().split()))
    for i in range(19)
]
win = 0
lst=[]
#이기는건 세로5개이상 가로5개이상 대각선 5개이상 역대각선 5개이상 
for i in range(19):
    for j in range(19):
        # x,y좌표 
        # 3,3이 지금 검은색(1) 
        #가로로 가거나 세로로 가거나 대각선으로 가거나. 
        if (arr[i][j]==1 and arr[i][j+1]==1 and arr[i][j+2]==1 and arr[i][j+3]==1 and arr[i][j+4]==1):
            win=1
            lst.append([i,j+2])
            break
        if (arr[i][j]==1 and arr[i+1][j+1]==1 and arr[i+2][j+2]==1 and arr[i+3][j+3]==1 and arr[i+4][j+4]==1):
            win=1
            lst.append([i+2,j+2])
            break
        if (arr[i][j]==1 and arr[i-1][j-1]==1 and arr[i-2][j-2]==1 and arr[i-3][j-3]==1 and arr[i-4][j-4]==1):
            win = 1 
            lst.append([i-2,j-2])
            break
        if (arr[i][j]==1 and arr[i+1][j]==1 and arr[i+2][j]==1 and arr[i+3][j]==1 and arr[i+4][j]==1):
            win = 1 
            lst.append([i+2,j])
            break
        if (arr[i][j]==2 and arr[i][j+1]==2 and arr[i][j+2]==2 and arr[i][j+3]==2 and arr[i][j+4]==2):
            win=2
            lst.append([i,j+2])
            break
        if(arr[i][j]==2 and arr[i+1][j+1]==2 and arr[i+2][j+2]==2 and arr[i+3][j+3]==2 and arr[i+4][j+4]==2):
            win=2
            lst.append([i+2,j+2])
            break
        if(arr[i][j]==2 and arr[i+1][j]==2 and arr[i+2][j]==2 and arr[i+3][j]==2 and arr[i+4][j]==2):
            win = 2
            lst.append([i+2,j])
            break
        if (arr[i][j]==2 and arr[i-1][j-1]==2 and arr[i-2][j-2]==2 and arr[i-3][j-3]==2 and arr[i-4][j-4]==2):
            win=2
            lst.append([i-2,j-2])
            break
        else:
            pass
print(win)
for i in range(len(lst[0])):
    print(lst[0][i]+1,end=" ")

    
                    