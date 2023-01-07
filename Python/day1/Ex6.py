"""
a = 2, b = 8
a + b = 10
2 + 8 = 10
"""
a = 2.1
b = 8
print(str(a) + " + " + str(b) + " = " + str(a+b))
print(a, "+", b, "=", a+b, sep=" ")
print("%.1f + %d = %.1f"%(a,b,a+b))
print("{0} + {1} = {2}".format(a,b,a+b))
print("{a} + {b} = {a+b}")
print(f"{a} + {b} = {a+b}")
print('*'*10)
print("-"*20)