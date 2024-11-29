a,b=map(int,input().split())
n = list(str(input()))

tenjinsu=0
for i in range(len(n)):
    tenjinsu = tenjinsu + pow(a,len(n)-(i+1))*int(n[i])

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
print(solution(tenjinsu,b))