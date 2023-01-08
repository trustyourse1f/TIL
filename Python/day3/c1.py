#n=0
#for i in range(5) :
 #   n+=abs(int(input(f"{i+1}번째 입력")))

#print(n)
n=0
nl=map(int,input("5개 정수 입력(구분자 공백):").split())
for i in nl:
   n+=abs(i)
print(n)
