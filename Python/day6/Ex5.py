"""
class A:
    __x="data"
    def __init__(self):
        self.__x=0
    def __f(self):
        print("함수동작")
    @classmethod
    def f(cls):
        print(cls.__x)
a=A()
#a.__x=10
#print(a.__x)
#a.__f()
#print(A.__x)
A.f()
"""
class A:
    def __init__(self):
        self.__x = 0
    def set_f(self,x):
        self.__x = x
    def get_f(self):
        return self.__x
a = A()
a.set_f(20)
print(a.get_f())