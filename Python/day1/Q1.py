"""
안녕하세요
print() 5번 사용해서 출력
"""
print("안",end="")
print("녕",end="")
print("하",end="")
print("세",end="")
print("요",end="")
"""
a=10,b=20
10+20=30
print() 1개 사용
2가지 방법
1. ,를 이용
2. f문자열을 이용
"""

a=10
b=20
print(a,"+",b,"=",a+b,sep="")
print(type(f"{a}+{b}={a+b}"))
