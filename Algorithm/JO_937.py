first_array=[list(map(int,input().split(" "))) for _ in range(2)]

second_array=[list(map(int,input().split(" "))) for _ in range(2)]

first_line=[]
second_line=[]
times_array=[]

for i in range(2):
    for j in range(3):
        if i==0:
            first_line.append(first_array[i][j]*second_array[i][j])
        else :
            second_line.append(first_array[i][j]*second_array[i][j])
times_array.append(first_line)
times_array.append(second_line)

print(times_array)