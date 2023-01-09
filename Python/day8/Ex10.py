import pickle
pickle.dump([1,2,3,4,5],open("data.p","wb"))
i_f=open("data.p","rb")
i=[]

l=pickle.load(open(i_f))
print(l)
l = pickle.load(open(i_f))
print(l)
