리스트 = []
반복횟수 = int(input())

for _ in range(반복횟수):
    리스트.append(int(input()))

for i in range(반복횟수):
    print(sorted(리스트)[i])