def plus(a, b):
    c = a + b
    return c
def minus(a, b):
    c = abs(a - b)
    return c
a = 2
b = 5

class cal():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def plus(self):
        self.p = self.a + self.b
    def minus(self):
        self.m = abs(self.a - self.b)
    
c = cal(3, 6)
c.plus()
print(c.p)
c.minus()
print(c.m)