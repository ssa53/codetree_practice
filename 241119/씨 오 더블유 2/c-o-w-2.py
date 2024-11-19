n = int(input())
lst = list(str(input()))
cnt_c = 0
cnt_o = 0
cnt_w = 0
for i in lst:
    if i == 'C':
        cnt_c += 1 
    elif i == 'O':
        cnt_o += 1
    elif i == 'W':
        cnt_w += 1
    else:
        pass

print(cnt_c*cnt_o*cnt_w)
