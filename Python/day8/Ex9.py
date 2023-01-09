l=[1,2,3,4,5]
try:
    x=l[5]
    print("동작")
    int("a")
    open()
except ValueError and TypeError:
    print("값 예외 발생")
except IndexError:
    print("인덱스 예외 발생")
except Exception:
    print("예외")