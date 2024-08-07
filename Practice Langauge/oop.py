# class Human:
#     def __init__(self, n, o):
#         self.name = n
#         self.occupation = o

#     def doWork(self):
#         if(self.occupation == 'tennis player'):
#             print(self.name, "plays tennis.")  
#         elif (self.occupation == 'cricket player'):
#             print(self.name, "plays cricket.")
#         else:
#             print(self.name, "is welaa")  
    

# abrar = Human('Abrar', 'cricket player')
# john = Human('John', 'tennis player')

# abrar.doWork()
# john.doWork()


# Inheritace
# class Vehicle:
#     def __init__(self, t, hR):
#         self.tires = t
#         self.hasRoof = hR

#     def getDetails(self):
#         print('I have',self.tires, 'tires')
#         print('I', 'have' if self.hasRoof  else 'do not have', 'roof')

# class Car(Vehicle):
#     def __init__(self):
#         super().__init__(4, True)
#         print('I am Car')

# class Bike(Vehicle):
#     def __init__(self):
#         super().__init__(2, False)
#         print('I am Bike')

# car = Car()
# car.getDetails()

# bike = Bike()
# bike.getDetails()

# # Multiple Inheritance
# class Father:
#     def gardening(self):
#         print('I love gardening')

# class Mother:
#     def cooking(self):
#         print('I love cooking')

# class Child(Father, Mother):
#     def playing(self):
#         print('I love playing')

# c = Child()
# c.playing()
# c.cooking()
# c.gardening()

# Multilevel Inheritance
# class GrandFather:
#     def shooting(self):
#         print('I love shooting')

# class Father(GrandFather):
#     def gardening(self):
#         print('I love gardening')

# class Child(Father):
#     def playing(self):
#         print('I love playing')

# c = Child()
# c.playing()
# c.gardening()
# c.shooting()

# Hybrid Inheritance
class GrandFather:
    def shooting(self):
        print('I love shooting')

class Father(GrandFather):
    def gardening(self):
        print('I love gardening')

class Mother:
    def cooking(self):
        print('I love cooking')

class Child(Father, Mother):
    def playing(self):
        print('I love playing')

c = Child()
c.playing()
c.cooking()
c.gardening()
c.shooting()