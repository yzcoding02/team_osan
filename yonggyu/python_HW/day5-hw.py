def 홀수(a):
    hs=[]
    for i in range(1,a*2):
        if i%2!=0:
            hs.append(i)
            hs.sort()
            hs.reverse()
    print(hs)
홀수(7)
