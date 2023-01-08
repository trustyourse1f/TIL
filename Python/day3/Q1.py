score=int(input("0점에서 100점 사이의 점수를 입력하세요.\n:"))

if score >=90 :
    print(f"{score}점은 A학점입니다.")

elif score >=80 :
    print(f"{score}점은 B학점입니다.")

elif score >=70 :
    print(f"{score}점은 C학점입니다.")

elif score >=60 :
    print(f"{score}점은 D학점입니다.")

elif score >=0 :
    print(f"{score}점은 F학점입니다.")

else :
    print("범위를 벗어났습니다.")