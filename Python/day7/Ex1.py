"""
from abc import *
class A(metaclass=ABCMeta):
    @abstractmethod
    def 추상메소드(self):
        pass
class B(A):
    def 추상메소드(self):
        print("오버라이딩")

B()
"""

class A:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return A(x,y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return A(x,y)
    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.y
        return A(x,y)
    def __floordiv__(self, other):
        x = self.x // other.x
        y = self.x // other.y
        return A(x,y)
t1 = A()
t2 = A()
class B:
    x = 0
    y = 0

t1=A(5,4)
t2=A(5,6)
print(t1.x,t1.y)
t1+t2
print(t1.x,t1.y)
c1=B()
c2=B()
print(c1.x,c1.y)
c1.x+c2.x
c1.y+c2.y
print(c1.x,c1.y)
