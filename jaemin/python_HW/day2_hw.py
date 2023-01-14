    
sum=0
for i in range(20,41):
    if i%3!=0:
        sum+=i
print(sum)


for i in range(50,101):
    if i%3==0:
        if i%4==0:
            print(i)


new=0
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
    
    if i%2==1:
        new+=i
print(sum-new)


axc=1
for i in range(10,31):
    if i%9==0:
        axc*=i
print(axc)