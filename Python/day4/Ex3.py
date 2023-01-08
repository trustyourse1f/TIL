def f(x,y):
    print(x,y)
    return x,y
def f1(x):
    x+=1
    return x
def f2(x):
    x[0]+=1
    return x
x=10
y=[1]
#print(f(x,20))
print(x)
print(f1(x))
print(x)
print(f2(y))
print(y)
