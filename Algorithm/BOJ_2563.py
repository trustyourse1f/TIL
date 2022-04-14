도화지 = [list([0]*100) for _ in range(100)]

색종이의_수 = int( input() )

for _ in range(색종이의_수):
    x,y = map(int, (input().split(" ")))
    for i in range(100-(y+10), 100-y):
        for j in range(x, x+10):
            도화지[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if 도화지[i][j] == 1:
            count+=1


print(count)