class A:
    def __init__(self,x):
        print("A생성자 동작")
        self.x = x
    def f(self):
        print("A의 함수")
class B(A):
    def __init__(self):
        super().__init__(10)
        print("B생성자 동작")

a = B()
b = A(10)
#a.f()
print(b.x)
print(a.x)