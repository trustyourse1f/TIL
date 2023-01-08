scoList = []
while True :
    print("------------------------------------------------")
    print("1.학생수 | 2.점수입력 | 3.점수리스트 | 4.분석 | 5.종료")
    print("------------------------------------------------")
    s = int(input("선택> "))
    stuNum = 0
    if s == 1:
        stuNum=int(input("학생수> "))
    elif s == 2:
        if stuNum == 0:
            continue
        for i in range (stuNum) :
            scoList.append(int(input(f"scores[{i}]> ")))
    elif s == 3:
        if stuNum == 0:
            continue
        for i in range (stuNum) :
            print(f"scores[{i}]: {scoList[i]}")
    elif s == 4:
        if stuNum == 0:
            continue
        sum = 0
        for i in range (len(scoList)) :
            sum += scoList[i]
        avg = sum / len(scoList)
        print(f"최고점수 : {max(scoList)}")
        print(f"평균점수 : {avg}")
    elif s == 5:
        break