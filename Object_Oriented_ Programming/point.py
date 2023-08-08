class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        print("drawing...")

    @classmethod
    def point_from_one(cls):
        return cls(1, 1)

    def __str__(self):
        return f"({self.a}, {self.b})"




p1 = Point(2, 3)
p2 = Point(3, 5)
p1.draw()
print(p1)
