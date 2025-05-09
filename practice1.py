class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fuck_you(self):
        return f"fuck you {self.firstname},{self.lastname}"


class Employee(Person):
    def __init__(self, firstname, lastname, job):
        super().__init__(firstname, lastname)
        self.job = job


amir = Employee("amir", "mahdi", "soltan")
print(amir.fuck_you())
