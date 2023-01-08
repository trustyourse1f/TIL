"""
class A:#클래스 선언
    필드=0#클래스필드
    def __init__(self,x=10):
        print("생성자 A동작")
        self.필드=10#인스턴스필드
a=A()
a=A(10)
"""

class M:
    def __init__(self):
        print("생성자 동작")
    def 메서드1(self):
        print("메서드1 동작")
    def 메서드2(self, x):
        print(x, "입력을 받는 메서드2 동작")
    def 메서드3(self):
        print("메서드3 동작")
        return 10
    def 메서드4(self, x, y):
        print(x, y, "메서드4 동작")
    def 메서드5(self, x):
        return f"{x}를 입력받는 메서드5 동작"
m = M()
m.메서드1()
m.메서드2(10)
m.메서드3()
m.메서드4(10,10)
print(m.메서드5(10))