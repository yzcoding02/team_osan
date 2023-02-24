# 1번
for i in range(3):
    print("안녕")
# 2번
sum = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum += i
print(sum)
# 3번
sum= 1
for i in range(1, 21):
    if i % 5 != 0:
        sum *= i
print(sum)
# 4번
for i in range(1,101):
    if i % 2 == 0:
        if i % 3 == 0:
            if i % 5 == 0:
                print(i)
# 5번
sum = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum += i
print(sum)