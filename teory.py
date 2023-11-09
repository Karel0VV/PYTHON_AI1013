# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         self.money = 2000
#         print("I am alive!")
#
# stepan = Student()
# print(stepan.height)
# print(stepan.money)
# stepan.money -= 500
# print(stepan.money)


# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         self.money = 2000
#         print("I am alive!")
#
# stepan = Student()
# print(stepan.height)
# print(stepan.money)
# stepan.money -= 500
# print(stepan.money)





# class Student:
#     amout_of_students = 0
#     def __init__(self, height = 160 ):
#         self.height = height
#         Student.amout_of_students += 1
#
# stepan = Student(height=180)
# print("Stepan",stepan.height, stepan.amout_of_students)
#
# katrin = Student(height=170)
# print("Stepan",katrin.height, katrin.amout_of_students)
#
# Oleg = Student()
# print("Stepan",Oleg.height, Oleg.amout_of_students)


class Student:
    amout_of_students = 0
    def __init__(self, height = 160 ):
        self.height = height
        Student.amout_of_students += 1

    def printHeight(self):
        print(self.height)

    def subMoney(self,countMoney = 0):
        self.money -= countMoney

    def printCountMoney(self):
        print(self.money)

    def subMoney(self,countMoney = 0):
        self.money -= countMoney
        Student.printCountMoney(self)



stepan = Student(height=180)
stepan.printHeight()
stepan.printCountMoney()
print("-"*20)

katrin = Student(height=170)
katrin.subMoney(200)

print("-"*20)


Oleg = Student()
