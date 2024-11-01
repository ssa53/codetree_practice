class you:
    def __init__(self,_id="codetree",level=10):
        self._id = _id
        self.level = level

_id_input,level_input = input().split()
_id_input = str(_id_input)
level_input = int(level_input)

codetree = you()
print ("user",codetree._id,"lv",codetree.level)

you = you(_id_input,level_input)

print("user",you._id,"lv",you.level)