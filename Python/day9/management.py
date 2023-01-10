from pickle import dump,load

냉장고 = []

class item:
    num = 0
    def __init__(self, 이름, 개수, 유통기한):
        self.이름 = 이름
        self.개수 = 개수
        self.유통기한 = 유통기한
        item.num += 1
    def __del__(self):
        item.num -= 1

#냉장고에 item 추가
def add_item():
    이름 = input("이름:")
    개수 = int(input("개수:"))
    유통기한 = input("유통기한:")
    냉장고.append(item(이름, 개수, 유통기한))

#냉장고 확인
def view():
    for i in range(len(냉장고)):
        print(f"이름:{냉장고[i].이름}")
        print(f"개수:{냉장고[i].개수}")
        print(f"유통기한:{냉장고[i].유통기한}")
        print("")

#냉장고에 있는 item 삭제
def delete():
    d = input("삭제할 item 이름:")
    for i in range(len(냉장고)) :
        if d == (냉장고[i].이름):
            del 냉장고[i]
            break

#저장
def save():
    w_f = open("data.p", 'wb')
    dump(냉장고, w_f)
    w_f.close()

try:
    i_f = open("data.p", "rb")
except:
    print("저장된 data가 없습니다.")
else:
    냉장고 = load(i_f)
    i_f.close()

run = False
while run != True:
    print("""--------냉장고--------
        1.추가
        2.확인
        3.삭제
        4.저장
        5.종료""")
    print("냉장고 내 item 수:",item.num)
    m = int(input(">>"))
    if m == 1:
        add_item()
    elif m == 2:
        view()
    elif m == 3:
        delete()
    elif m == 4:
        save()
    elif m == 5:
        exit = input("종료하시겠습니까? y/n:")
        if exit == 'y':
            break
        else:
            continue
    else :
        continue