from random import *
randnum=randint(1,100)
trynum=1
guess = int(input("1에서 100까지의 숫자를 입력하십시오."))
while guess!=randnum :
    if guess < randnum :
        print("Up")
    else :
        print("Down")
    trynum +=1
    guess = int(input("1에서 100까지의 숫자를 입력하십시오."))


print(f"{trynum}회째 정답!")