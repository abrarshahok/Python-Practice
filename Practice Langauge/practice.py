# def pow(val, power):
#     return val**power

# print(pow(2,3))

# myc_bal = 188
# bal_pit = 247
# total_distance = myc_bal + bal_pit
# mph = 65
# time = total_distance / mph

# print(round(time,2))

# message = "Hello, World!"
# print(message)
# print(message[::-1])
# print(message[3:5])
# print(message[:5])
# print(message[2::])

# message = "Hello "
# number = 20

# print(message + str(number))

# list1 = ['one','two']
# list2 = ['three','four', 'five']

# print(list1)
# print(list2)

# list2.append('six')
# list1.insert(0, 'zero')

# list = list1 + list2

# print(list)
# print(len(list))
# print(list[::-1])

# print('one' in list1)
# print('one' in list2)

# print('one' not in list1)
# print('one' not in list2)


# age = int(input('Enter your age: '))

# if(age >= 18):
#     print('Eligible')
# else:
#     print('In-eligible')    

# for i in range(1,11):
#     print(i)

# expenses = [2312, 3432, 1234, 5323, 2354]
# total = 0

# for item in expenses:
#     total += item 

# print(total)

# total = 0
# for i in range(len(expenses)):
#     print('Month: ', i+1, 'Expense: ',expenses[i])
#     total += expenses[i] 

# print('Total: ',total)

# i = 0
# total = 0
# while i < len(expenses):
#     print('Month: ', i + 1, 'Expense: ',expenses[i])
#     total += expenses[i] 
#     i += 1

# print('Total: ', total)

# def getTotal(expenses):
#     total = 0
    
#     for i in range(len(expenses)):
#         total += expenses[i] 

#     return total

# def getSum(*args):
#     total = 0
    
#     for i in args:
#         total += i 

#     return total

# expenses = [2312, 3432, 1234, 5323, 2354]
# total = getTotal(expenses)
# sum = getSum(1,2,3,4,5)
# print(total)
# print(sum)

# dict = {}

# for i in range(5):
#     dict['Emp ' + str(i + 1)] = str(i + 1) + '231435648'

# for i in range(5):
#     print(dict['Emp: ' + str(i + 1)])

# del dict['Emp ' + str(1)]

# for key in dict:
#     print(key, ' => ', dict[key])

# for k,v in dict.items():
#     print(k, ' => ', v)
# point = (3, 9)

# import myModule

# list = myModule.sortList([1,3,2,5,6,8,7])
# print(list)

