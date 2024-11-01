class my:
    def __init__(self,name="codetree",code=50):
        self.name=name
        self.code=code

name,code = input().split()
product0 = my()
product1 = my(str(name),int(code))
print("product",product0.code,"is",product0.name)
print("product",product1.code,"is",product1.name)