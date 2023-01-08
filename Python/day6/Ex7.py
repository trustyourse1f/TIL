"""
class A:
    def __init__(self):
        print("A의 생성자 동작")
    def __f(self):
        print("나만쓰는 함수")
    def g(self):
        self.__f()
    def c(self):
        pass

class B(A) :
    def __init__(self):
        super().__init__()
        print("B의 생성자 동작")
class C(B):
    def __init__(self):
        super().__init__()
        print("C의 생성자 동작")


a=C()
"""

class A:
    def __init__(self):
        print("A의 생성자 동작")

class B(A):
    def __init__(self):
        super().__init__()
        print("B의 생성자 동작")
    def f(self):
        print("B의 함수")

class C(A):
    def __init__(self):
        super(C, self).__init__()
        print("C의 생성자 동작")
    def f(self):
        print("C의 함수")

class D(B,C):
    def __init__(self):
        super(D, self).__init__()
        print("D의 생성자 동작")
        self.f()
D()