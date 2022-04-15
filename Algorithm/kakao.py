def solution(s):
    extract = ""
    for i in range(len(s)):
        if '1' <= s[i] <= '9':
            extract += s[i]
            continue
        for j in range(i+1, len(s)+1):
            if s[i: j] == 'one':
                extract += '1'
                break
            elif s[i: j] == 'two':
                extract += '2'
                break
            elif s[i: j] == 'three':
                extract += '3'
                break
            elif s[i: j] == 'four':
                extract += '4'
                break
            elif s[i: j] == 'five':
                extract += '5'
                break
            elif s[i: j] == 'six':
                extract += '6'
                break
            elif s[i: j] == 'seven':
                extract += '7'
                break
            elif s[i: j] == 'eight':
                extract += '8'
                break
            elif s[i: j] == 'nine':
                extract += '9'
                break     
    answer = int(extract)
    return answer

print(solution("oneoneoneone"))   