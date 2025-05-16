# first project
# class Car ():
#     def __init__(self,name,speed):
#         self.name=name
#         self.speed=speed
#     def __str__(self):
#         return f"Car : {self.name} , maxspeed : {self.speed}"


# second project
# class Animals ():
#     def move (self):
#         return "animal is moving "
# class lion (Animals):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#     def move(self):
#         return f"{self.name} is moving"
# lion=lion("lion")
# print(lion.move())
# third third
# class Animals :
#     def __init__(self,name):
#         self.name  = name
#     def speak (self):
#         return " The animal is speaking "
# class Bird (Animals):
#     def __init__(self,name):
#         super().__init__(name)
#     def speak (self):
#         return f"{self.name} is speaking "
# kaftar= Bird("kaftar")
# print (kaftar.speak())
# fourth project
# class Animal :
#     def speak (self, name = None):
#         if name:
#             return f"it is The  {name } making sound right know "
#         else :
#             return "it is makig sound right know"
#     def sound_mean(self,Type = None):
#         if Type:
#             return f"sorry but Im a {Type} you cant understand what im saying right know "
#         else :
#             return "sorry but I cant understand what im saying right know"
# class Cat (Animal):
#     def __init__(self,name):
#         self.name = name
#         self.Type = "Cat"
#     def speak (self):
#         do=super().speak(self.name )
#         mean=super().sound_mean(self.Type)
#         return  do + mean
# fandogh = Cat("fandogh")
# print (fandogh.speak())
# fivth project
# class Animals:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return " The animal is speaking "


# class Bird(Animals):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return f"{self.name} is speaking "


# parrot = Bird("parrot")
# print(isinstance(parrot,Animals))
# sixth project
# class Person :
#     def __init__ (self , __age):
#         self.__age=__age
#     def age (self):
#         return f"Age : {self.__age}"
# Amir=Person(25)
# print(Amir.age())

# seventh project


# class Student:
#     def __init__(self):
#         self.__name, self.__age, self.__grade = None, None, None

#     def set_info(self):
#         self.__name, self.__age, self.__grade = input(
#             "enter your informaition :"
#         ).split(" ")
#         self.__age = int(self.__age)

#     def get_info(self):
#         return f" name : {self.__name} & Age : {self.__age}  & grade : {self.__grade}"


# amir = Student()
# amir.set_info()
# print(amir.get_info())


# eighth project
# class Calculator:
#     def __init__(self):
#         pass

#     def get_number(self):
#         self.Numbers = input("Enter your Number : ").split()

#     def __Calculate(self):
#         self.calculate_number = 0
#         for Num in self.Numbers:
#             self.calculate_number += int(Num)
#         return self.calculate_number

#     def get_calculate_number(self):
#         return self.__Calculate()


# number = Calculator()
# number.get_number()
# print(number.get_calculate_number())

# ninth project


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f" args : {args} & kwargs : {kwargs}")
#         print(func(*args, **kwargs))
#         print(f" end of {func.__name__} function")

#     return wrapper


# @my_decorator
# def plus(*args):
#     Total = 0
#     for num in args:
#         Total += num
#     return Total


# plus(2, 4, 6, 3, 5, 1, 2)

#  tenth project


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f" args : {args} & kwargs : {kwargs}")
        print(func(*args, **kwargs))
        print(f" end of {func.__name__} function")

    return wrapper


@my_decorator
def plus(*args):
    Total = 0
    for num in args:
        Total += num
    return Total


plus(2, 4, 6, 3, 5, 1, 2)
