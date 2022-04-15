s = input()
d={}
for key in s.split(" "):
    d[key]=0

for key in s.split(" "):
    d[key] +=1

print(d.keys(min(d.values())))
print(min(d.values()))