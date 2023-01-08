"""
a,b=map(int(input("입력:").split()))
if a>b:
    max_v=a
    min_v=b
else:
    max_v=b
    max_v=a

print(f"최댓값{max_v}\n최솟값:{min_v}")
max_v= b if a<b else a
min_v= a if a<b else b
print(f"최댓값{max_v}\n최솟값:{min_v}")
"""
a,b,c=map(int,input("정수 3개 입력:").split())
print(a if (a<b)&(a<c) else (b if b<c else c))
