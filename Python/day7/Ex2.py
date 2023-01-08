class 은행:
    은행계좌정보={}
    def __init__(self,계좌번호,계좌주,초기입금):
        self.계좌번호=계좌번호
        self.계좌주=계좌주
        self.초기입금=초기입금

def 생성():
    print("계좌생성")
    계좌번호=input("계좌번호:")
    if 계좌번호 in 은행.은행계좌정보:
        print("이미 등록된 계좌번호 입니다.")
    else:
        계좌주=input("계좌주:")
        초기입금=int(input("초기입금액:"))
        은행.은행계좌정보[계좌번호]=은행(계좌번호,계좌주,초기입금)
def 목록():
    print("계좌목록")
    print("계좌번호|계좌주|예금액")
    for i in 은행.은행계좌정보.values():
        print(i.계좌번호,end="|")
        print(i.계좌주,end="|")
        print(i.초기입금)

def 입금():
    print("예금")
    계좌번호=input("계좌번호:")
    if 계좌번호 not in 은행.은행계좌정보:
        print("등록된 계좌가 없습니다.")
        return
    확인계좌=은행.은행계좌정보[계좌번호]
    예금액=int(input("예금액:"))
    확인계좌.초기입금+=예금액
    print("예금성공")

def 출금():
    print("출금")
    계좌번호 = input("계좌번호:")
    if 계좌번호 not in 은행.은행계좌정보:
        print("등록된 계좌가 없습니다.")
        return
    확인계좌 = 은행.은행계좌정보[계좌번호]
    출금액 = int(input("출금액:"))
    if 확인계좌.초기입금<출금액:
        print("잔고가 부족합니다.")
        return
    확인계좌.초기입금 -= 출금액
    print("출금성공")

def 종료():
    print("프로그램 종료")
    return True

run=False
m=생성,목록,입금,출금,종료
while not run:
    idx=int(input("""
    -------------------------------------
    1.계좌생성|2.계좌목록|3.예금|4.출금|5.종료
    -------------------------------------\n"""))
    if idx not in [1,2,3,4,5]:
        continue
    run=m[idx-1]()