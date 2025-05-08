# first project
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        return f" The {self.color} Car model {self.model} is driving "

    def __str__(self):
        return f" this is {self.color} Car and it model is {self.model}"


pride = Car("red", "pride")
print(pride)


# second project
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        return f"{self.name} has study"

    def increase_grade(self):
        return f"{self.name} score is {int (self.grade) +1} "


Amir = Student("Amir", 20, 18)
print(Amir.increase_grade())


# third project
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        return f"The {self.title} is being read"

    def __len__(self):
        return self.pages


math = Book("math", "tesla", 354)
print(math.read())
print(len(math))


# fourth project
class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def tick(self):
        hour = self.hour
        minute = self.minute
        minute += 1
        if minute >= 60:
            hour += 1
            minute = 00
        if hour >= 24:
            hour = 00
        return f"time is {hour}:{minute} "

    def __str__(self):
        return f"time is {self.hour}:{self.minute} "


now = Clock(23, 59)
print(now.tick())
print(now)


# من این جا برای تمرین خودم از date, datetime استفاده نکردم ولی بهم بگو توی tick چرا 00 رو نشون نداد چیکار کنم از این به بعد نشون بده
# fivth project
class Wallet:
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money

    def add_money(self, amount):
        self.money += amount
        return f"Money was succesfully deposited \n your amount is {self.money}"

    def spend_money(self, amount):
        if amount > self.money:
            return f"not enoph money you have {amount-self.money} less money to pay"
        else:
            self.money -= amount
            return f"your amount is {self.money}"


omid = Wallet("omid", 1.23)
print(omid.add_money(2))
print(omid.spend_money(6))
