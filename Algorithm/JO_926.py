first_array=[list(map(int,input().split(" "))) for _ in range(2)]

second_array=[list(map(int,input().split(" "))) for _ in range(2)]

for i in range(2):
    for j in range(4):
        print(first_array[i][j]*second_array[i][j],end=" ")
    print()