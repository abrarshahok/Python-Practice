# list  = [1,2,3,4,5,6]

# even = []

# for n in list:
#     if(n % 2 == 0):
#         even.append(n)

#   output   loop       condition
# even = [i for i in list if i % 2 == 0]

# print(even)

# square_nums = [i*i for i in list]
# print(square_nums)

# dup  = [1,2,3,4,5,6,1,2]
# s = set(dup)
# print(s)

# even_s = {i for i in s if i % 2 == 0}
# print(even_s)

cities = ['mumbai', 'new york', 'paris']
countries = ['india', 'usa', 'france']

z = zip(countries, cities)

# for i in z:
#     print(i)

data = {country:city for country,city in z}
print(data)
