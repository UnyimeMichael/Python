#   the parent class in this file is Animal
#   the purpose of inheritance is to ADOPT a BEHAVIOUR that is common amongst classes.
class Animal:
    def eat(self):
        print("Eating...")

    #     if I know the value of the instance, I can just initialize it directly in the constructor
    #     buh if I don't, I'd have t pass it as a parameter inside the constructor method
    def __init__(self):
        self.age = 10


# the moment a constructor is defined in the subclass, it overrides the parent constructor
# thereby preventing the subclass from accessing the instance variables in the parent class.
class Mammal(Animal):
    # for class Mammal to access the parent's instance variables, you have to reference the parent
    # class's constructor using the keyword 'super'
    def __init__(self):
        super().__init__()
        self.weight = 45

    def walk(self):
        print("I am walking...")


# python supports multiple inheritance...

class Fish(Mammal):
    def walk(self):
        print("I am swimming...")


#   instance variables(attributes) can also be inherited from the parent(base) class.
#   constructors are also inherited from the parent(base) class.

m = Mammal()
m.eat()
f = Fish()
print(m.age)
f.eat()
print(m.weight)
print(f.age)
print(isinstance(Mammal, object))
print(issubclass(Fish, object))
