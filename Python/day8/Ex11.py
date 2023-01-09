import pickle
pickle.dump([1,2,3,4,5], open("data2.p","wb"))
try:
    open("data1.p", "rb")
except:
    print("예외")
    x = []
else:
    x = pickle.load(open("data1.p","rb"))
    print("예외 미발생 시 동작")
