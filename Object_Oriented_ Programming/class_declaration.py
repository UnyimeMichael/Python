class Human:
    number_of_eyes = 2

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"hello {self.name}")

    def walk(self):
        print(f"{self.name} can walk")

    @classmethod
    def blue_eyes(cls):
        pass

    def __str__(self):
        return f"{self.name}"


# object creation(instantiation) of class and initializing an object
human1 = Human("esther")
human2 = Human("torin")
human1.greet()
human2.greet()
human1.walk()
human2.walk()
print(human1.name)
print(human2.name)
print(type(human2))
print(isinstance(human1, Human))
print(human1)
print(Human.number_of_eyes)
print(human1.number_of_eyes)