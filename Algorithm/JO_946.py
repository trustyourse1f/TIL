num = int(input())
dic = {}
for _ in range (num):
    country, cap_city = input().split(" ")
    dic[country] = cap_city

print(dic.get(input(), "Unknown Country"))