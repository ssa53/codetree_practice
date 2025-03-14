def YESORNO(n):
    if (n//10 + n%10)%5 == 0 and n%2==0:
        return "Yes"
    else:
        return "No"
    
n = int(input())
print(YESORNO(n))