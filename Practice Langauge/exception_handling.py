num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 1: "))

try:
    sum = num1 / num2
    print(sum)
except Exception as exp:
    print('Exception: ', exp)    