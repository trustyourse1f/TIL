"""
문자열=input()
for i in range(len(문자열)):
    if 문자열[i]=='(':
        왼손구분=i
    elif 문자열[i]==')':
        오른손구분=i+1
왼손=문자열[:왼손구분]
오른손=문자열[오른손구분:]

왼손의_잔상=0
for i in range(len(왼손)):
    if '@' in 왼손[i]:
        왼손의_잔상+=1

오른손의_잔상=0
for i in range(len(오른손)):
    if '@' in 오른손[i]:
       오른손의_잔상+=1 

print(왼손의_잔상, 오른손의_잔상)
"""
냥냥펀치=input()
for i in range(len(냥냥펀치)):
    if 냥냥펀치[i]=='(':
        왼손=냥냥펀치[:i]
        오른손=냥냥펀치[i:]

print( 왼손.count('@'),오른손.count('@'))