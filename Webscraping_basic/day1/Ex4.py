from urllib.request import urlopen
f = urlopen("http://www.hanbit.co.kr")
f1 = urlopen("http://www.naver.com")
print(f)
#print(f.read())
print(f.status)
print(f1)
print(f1.status)
print(f.getheader("Content-Type"))