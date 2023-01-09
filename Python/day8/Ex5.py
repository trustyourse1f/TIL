from collections import deque
l = deque()
l = []
l.append(10)
l.append(30)
l.append(20)
print(l)
print(l.pop())
print(l)
l = []
l.append(10)
l.append(30)
l.append(20)
l.pop(0)
l1 = list("data")
l2 = deque("data")
print(l1)
print(l2)