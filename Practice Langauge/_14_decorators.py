import time as t

def time_it(func):
    def wrapper(*args, **kargs):
        start = t.time()
        result = func(*args, **kargs)
        end = t.time()
        print(func.__name__,'took: ' + str((end-start)*1000) + ' ms')
        return result
    return wrapper

@time_it
def calc_square(numbers):
    res = [i*i for i in numbers]
    return res

@time_it
def calc_cube(numbers):
    res = [i*i*i for i in numbers]
    return res

numbers = range(1,100000)
calc_square(numbers)
calc_cube(numbers)