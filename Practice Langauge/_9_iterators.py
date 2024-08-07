
# a = [1,2,3,4]

# itr = iter(a)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# itr = reversed(a)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

class RemoteControl:
    def __init__(self):  
        self.channels = ['C1','C2','C3','C4','C5']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if(self.index == len(self.channels)):
            raise StopIteration

        return self.channels[self.index]
        

rc = RemoteControl()
itr = iter(rc)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))