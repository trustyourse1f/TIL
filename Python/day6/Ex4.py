
class 클래스이름:
    클래스필드 = "클래스필드"
    def __init__(self):
        self.인스턴스필드="인스턴스필드"
    def f(self):
        self.인스턴스필드2 = "data"
        print("인스턴스메소드 동작")
        print(self.클래스필드, "에 접근")
        print(self.인스턴스필드, "에 접근")
    @classmethod
    def 클래스메소드(cls):
        print("클래스메소드동작")
        print(cls.클래스필드+"에 접근")
        #print(cls.인스턴스필드, "에 접근")

#클래스에서 클래스멤버 접근 가능
#클래스에서 인스턴스멤버 접근 불가능 (클래스이름.인스턴스메소드() 불가능)
클래스이름.클래스메소드()
"""
print(클래스이름.클래스필드)
인스턴스=클래스이름()
print(인스턴스.인스턴스필드)
인스턴스.f()
print(인스턴스.인스턴스필드2)
print(인스턴스.클래스필드)


class A:
    c_f=0
    def __init__(self):
        self.i_f=100

print(A.c_f)
a=A()
print(a.i_f)
print(a.c_f)
a1=A()
print(a1.i_f)
print(a1.c_f)
A.c_f=300
print(A.c_f)
print(a.c_f)
print(a1.c_f)
a.c_f=20
print(A.c_f)
print(a.c_f)
print(a1.c_f)
A.c_f=100
print(A.c_f)
print(a.c_f)
print(a1.c_f)
"""