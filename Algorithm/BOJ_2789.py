"""
cambridge='CAMBRIDGE'
입력=input()
새_문자열=""

for i in range(len(입력)):
    for j in range(len(cambridge)):
        if 입력[i] != cambridge[j]:
            if j==len(cambridge)-1:
                새_문자열+=입력[i]
        else:
             break 
            
print(새_문자열)
"""

cambridge="CAMBRIDGE"
검열문자열=input()
for i in 검열문자열:
    if i not in cambridge:
        print(i,end="")