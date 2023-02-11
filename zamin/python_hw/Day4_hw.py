
#최대공약수
def 최공약(a, b,c):
    for i in range(min(a, b,c), 0, -1):
        if a % i == 0 & b % i == 0&c%i==0:
            return i
결과=최공약(1000,3000,10)
print(결과)