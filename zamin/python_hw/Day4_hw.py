
#최대공약수
def 최공약(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 & b % i == 0:
            return i
최공약(10,24)

    
