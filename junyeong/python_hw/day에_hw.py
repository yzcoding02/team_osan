
def 홀수(a):
    홀수우=[]
    for i in range(1,a*2):
        if i%2!=0:
            홀수우.reverse()
            홀수우.sort()
            홀수우.append(i)
    print(홀수우)
홀수(5)