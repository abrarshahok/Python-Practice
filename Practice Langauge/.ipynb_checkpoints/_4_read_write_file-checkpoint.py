f = open("/Users/abrar/Python Practice/pract.txt", "w")

f.write('''Teacher: "Good morning, class. Today, we'll be learning about the water cycle. Can anyone tell me what evaporation is?"
Student: "Evaporation is when water turns into vapor and rises into the air."
Teacher: "That's correct! And what causes evaporation to happen?"
Student: "The heat from the sun causes water to evaporate."
Teacher: "Excellent. Let's talk about the next stage, which is condensation."''')

f.close()

# f = open("/Users/abrar/Python Practice/pract.txt", "a")
# f.write('\nHello World Again')
# f.close()

f = open("/Users/abrar/Python Practice/pract.txt", "r")
# s = f.read()
# # f.close()
# print(s)

words = []

for line in f:
    words = line.split(' ')
    # print(line)

print(len(words))    