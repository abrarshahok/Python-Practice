# def gen():
#     yield "C1"
#     yield "C2"
#     yield "C3"

# itr = gen()
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

def fib_gen(n):
    a, b = 0, 1
    while(n > 0):
        yield a
        a, b = b, a+b
        n -= 1

for i in fib_gen(13):
    print(i)