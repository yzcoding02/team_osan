def GCM(a,b):
    for i in range(min(a,b),0,-1):
            if a%i==0 and b%i==0:
                 return i
결과=GCM(1000,3000)
print(결과)


def GCM(a,b,c):
    for i in range(min(a,b,c),0,-1):
            if a%i==0 and b%i==0 and c%i==0:
                 return i
결과=GCM(3,6,9)
print(결과)