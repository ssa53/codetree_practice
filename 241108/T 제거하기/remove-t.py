s = str(input())
t = str(input())
def get_rid(s,t):
    if t not in s:
        return s 
    return get_rid(s.replace(t,'',1),t)

print(get_rid(s,t))