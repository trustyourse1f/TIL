자동차_리스트=[]
i=0
class Car():
    def 정보입력(self,이름,엔진_가격,타이어_가격,옵션,옵션_이름,최고속도,구매_가격=0):
        self.이름 = 이름
        self.엔진_가격 = int(엔진_가격)
        self.타이어_가격 = int(타이어_가격)
        self.옵션 = 옵션
        self.옵션_이름 = 옵션_이름
        self.최고속도 = int(최고속도)
        self.구매_가격 = self.엔진_가격+self.타이어_가격
    def 목록보기(self):
        return f"이름:{self.이름}\n엔진 가격:{self.엔진_가격}\n타이어 가격:{self.타이어_가격}\n옵션:{self.옵션}\n옵션 이름:{self.옵션_이름}\n최고속도:{self.최고속도}\n"
    def 구매_가격_조회(self):
        return f"{self.이름}: {self.구매_가격}원"
    def 옵션이_있는_자동차_정보_조회(self):
        if self.옵션 == "있음":
            return f"{self.이름}:있음"
        else :
            return f"{self.이름}:없음"

while True:
    print("#### 자동차 정보 프로그램 ####")
    print("1. 자동차 정보 입력")
    print("2. 저장된 목록 보기")
    print("3. 각 자동차의 구매 가격 조회")
    print("4. 옵션이 있는 자동차 정보 조회")
    print("5. 빠른 자동차와 느린 자동차의 속도차 조회")
    print("6. 프로그램 이용종료")
    print("###########################")
    n=int(input("입력:"))
    if n==1:
        자동차_리스트.append(Car())
        이름 = input("이름:")
        엔진_가격 = int(input("엔진 가격:"))
        타이어_가격 = int(input("타이어 가격:"))
        옵션 = input("있음/없음:")
        옵션_이름 = input("옵션이름:")
        최고속도 = int(input("최고속도:"))
        while True:
            if 자동차_리스트[i] != None:
                자동차_리스트[i].정보입력(이름,엔진_가격,타이어_가격,옵션,옵션_이름,최고속도)
                i += 1
                break
    elif n == 2:
        for i in range (len(자동차_리스트)):
            print(자동차_리스트[i].목록보기())
    elif n == 3:
        for i in range (len(자동차_리스트)):
            print(자동차_리스트[i].구매_가격_조회())
    elif n == 4:
        for i in range(len(자동차_리스트)):
            print(자동차_리스트[i].옵션이_있는_자동차_정보_조회())
    elif n == 5:
        l = []
        for i in range (len(자동차_리스트)):
            l.append(자동차_리스트[i].최고속도)
        print(max(l)-min(l))
    elif n == 6:
        break
    else:
        continue