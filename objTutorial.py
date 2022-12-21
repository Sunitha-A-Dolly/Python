import self as self


class student:
    def __init__(self, rollno, grade):
        self.rollno = rollno
        self.grade = grade

    def accept(self):
        self.rollno = int(input("Enter rollno"))
        self.grade = input("Enter grade")

    def display(self):
        print("Roll no", self.rollno)
        print("grade", self.grade)


class Staff:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def accept(self):
        self.name = input("Enter name")
        if __class__ == "Staff":
            self.grade = input("Enter grade")

    def display(self):
        print("name", self.name)
        if __class__ == "Staff":
            print("grade", self.grade)


class School(student, Staff):
    def accept(self):
        student.accept(self)
        Staff.accept(self)

    def display(self):
        student.display(self)
        Staff.display(self)


x = School(5, "c")
x.accept()
x.display()
