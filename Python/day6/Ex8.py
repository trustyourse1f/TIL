"""
class A:
    def f(self):
        print("A의 함수")
class B(A):
    def f(self):
        print("B의 함수")
a=B()
a.f()
"""
class 동물:
    def 소리(self):
        pass

class 강아지(동물):
    def 소리(self):
        return "멍멍"

class 고양이(동물):
    def 소리(self):
        return "야옹"

class 닭(동물):
    def 소리(self):
        return "꼬끼오"

l=[강아지(),고양이(),닭()]
for i in l:
    print(i.소리())