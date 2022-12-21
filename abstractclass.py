from abc import ABC, abstractmethod


class School(ABC):
    @abstractmethod
    def getstudent(self):
        pass


class Student(School):
    def getstudent(self):
        print("No entry")


x = Student()
print(x)
