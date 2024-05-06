def sortList(lis):
    size = len(lis)
    for i in range(size):
        for j in range(size-1):
            if(lis[i] < lis[j]):
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
    return lis

def addNums(*args):
    sum = 0
    for num in args:
        sum += num;
    return sum

def printValues(**args):
    for i in args:
        print(i,args[i])
