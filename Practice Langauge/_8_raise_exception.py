# try:
#     raise MemoryError('Memory error!')
# except MemoryError as me:
#     print(me)


# user defined exception
class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def print_exception(self):
        print('User defined exception:',self.msg)

    def handle(self):
        print('Take detour')

try:
    raise Accident('Accident occurred!')
except Accident as acc:
    acc.print_exception()
finally:
    print('End Here!')
    