from abc import ABC, abstractmethod


#   The essence of using abstract method is to have uniform methods across other subclasses.
#   abstract method should be declared in the parent class and implemented in the subclasses as the children wish.


class InvalidOperationError(Exception):
    pass


#   Exception is the base class for all exceptions that will be passed in the classes
#     constructors are used to initialize variables.

class Stream(ABC):
    def __init__(self):
        self.is_open = False

    def open(self):
        if self.is_open:
            raise InvalidOperationError("Invalid operation, cannot open")
        self.is_open = True

    @abstractmethod
    def write(self):
        pass


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network...")

    def write(self):
        print("writing to a network stream")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")

    def write(self):
        print("writing to a memory stream")
