# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create a class
class User:
    # constructor--function that runs when enstantiate an object from a class
    def __init__(self, name, email, age):
        # use "self" in standard python class instead of "this"
        self.name = name
        self.email = email
        self.age = age

# create methods to be run on the class
    def greeting(self):
        return f"my name is {self.name} and I am {self.age}"

    def has_birthday(self):
        self.age += 1

# extend class
class Customer(User):
    # constructor
    def __init__(self, name, email, age):
        # use "self" in standard python class instead of "this"
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"my name is {self.name} and my balance is {self.balance}"

# initialize user object
katie = User("Katie", "katie@katie.com", 20)
print(type(katie))
print(katie.name)

katie.has_birthday()
print(katie.greeting())

# initialize a customer object
janet = Customer("Janet", "janet@janet.com", 25)
janet.setBalance(500)
print(janet.greeting())