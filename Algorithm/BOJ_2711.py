T=int(input())
for i in range(T):
    위치, 문자열=input().split()
    print(문자열[:int(위치)-1]+문자열[int(위치):])