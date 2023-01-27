a=0
while a<3:
    print("숙제다")
    a+=1

a=1
sum=0
while a<11:
    if a%2!=0:
        sum+=a
    a+=1
print(sum)

a=1
mul=1
while a<21:
    if a%5!=0:
        mul*=a
    a+=1
print(mul)


a=1
while a<101:
    if a%2==0:
        if a%3==0:
            if a%5==0:  
              print(a) 
    a+=1


a=1
sum=0
sum2=0
while a<101:
    if a%2==0:
        sum+=a
    if a%2!=0:
        sum2+=a
    a+=1
print(sum-sum2)

