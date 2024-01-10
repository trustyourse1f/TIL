import re
#. 문자
#^ 시작
#$ 끝
l=["abcd","adcd","accd","abdc"]
ck=re.compile("a.cd")
def print_t(str):
    if str:
        print("일치문자",str.group())
        print("입력문자", str.string)
        print("일치문자 시작", str.start())
        print("일치문자 끝", str.end())
        print("일치문자 시작, 끝", str.span())
    else:
        print("일치 없음")
for i in l:
    str=ck.match(i)
    print_t(str)
    print("일치", ck.search(i))
    print("all_data", ck.findall(i))


#print(ck.search("data"))
#print(ck.findall("da"))
#원하는 형태에 따른 문자열 선택:정규식
#match("문자열"):처음부터 일치
#search("문자열"): 일치하는 문자 있는지 확인
#findall("문자열"):일치하는 모든 것의 리스트 출력