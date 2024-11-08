a,b,c = map(int,input().split())
def magic(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return (n*3)-20

print(magic(a),magic(b),magic(c))