class MyChangedString:
    def __init__(self, name, avg):
        self.avg = avg
        self.name = name

    def __str__(self):
        return f"{self.name} average is {self.avg}"

"""
class CheckOpOverloading:
    def __init__(self,  int x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x * other.x
"""

X = MyChangedString("Sundar", 80)

print(X)
