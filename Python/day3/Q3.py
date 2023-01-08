a,b=map(int,input("입력\n").split())

if a<b :
    print(f"출력\n{a*10} {b//10}",end=(""))
else :
    print(f"출력\n{b*10} {a//10}",end=(""))