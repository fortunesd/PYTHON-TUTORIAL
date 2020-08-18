# In python a class is a blueprint for creating objects. an object is actually anything ypu can create in python and it has properties and functions(methods)
# Almost everything in python is an objects, thats why python is an object oreinted programming languague(oop)

# Create class

class Students:
    # constructor is actually a method or function that helps a class to initialize the agurment used in the class
    def __init__(self, name, email, age):
        self.name = name 
        self.email = email
        self.age = age 
    def greeting(self):
        return f'i am a student with name {self.name} and i am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extend class (inheritance)

class studentRep(Students):
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age 
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'i am the class rep with name {self.name} and i am {self.age} and my balance is {self.balance}'

# Create an object of class students
fortunes = Students('Onyekwere Fortunes', 'onyekwerefortunes1@gmail.com', 21)

# Create an object of class studentRep
joshua = studentRep('Ndubueze Joshua', 'josheze58@gmail.com', 20)

joshua.set_balance(800)
print(joshua.greeting())