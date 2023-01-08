"""
def f(x,y):
    print(f"x={x},y={y}")
# #기본입력
f(1,2) #순서입력
f(y=1,x=2) #지정입력

def d_f(y,x=1):
    print(x)
d_f(1)
d_f(10,)
"""
def f(*x):
    print(x)

f(1)

f((1,2,3,4))

f(1,2,3,4)