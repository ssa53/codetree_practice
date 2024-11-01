class my:
    def __init__(self,code,color,sec):
        self.code=code
        self.color=color
        self.sec=sec

code,color,sec = input().split()
bomb1 = my(str(code),str(color),int(sec))

print("code :",bomb1.code)
print("color :",bomb1.color)
print("second :",bomb1.sec)