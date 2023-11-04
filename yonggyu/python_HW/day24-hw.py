def error_print(opt):
    print(f"There is no option[{opt}]")

def find_divisor(num):
    divisor={1}
    for i in range(2,num+1):
        if num%i==0:
            divisor.add(i)
    return divisor
def find_GCD(num1,num2,num3):
    d1=find_divisor(num1)
    d2=find_divisor(num2)
    d3=find_divisor(num3)
    return max(d1&d2&d3)
def find_LCM(num1,num2,num3):
    d1=find_divisor(num1)
    d2=find_divisor(num2)
    d3=find_divisor(num3)
    return max(d1&d2&d3)*(num1/max(d1&d2&d3))*(num2/max(d1&d2&d3))*(num3/max(d1&d2&d3))
def calculate(num1,num2,num3,opt):
    if opt==1:
        print(f"GCD is {find_GCD(num1,num2,num3)}")
    elif opt==2:
        print(f"LCM is {find_LCM(num1,num2,num3)}")
    else:
        error_print(opt)
if __name__=="__main__":
    print("==============================================================================================")
    num1=input("[first number]+[enter]:")
    num2=input("[second number]+[enter]:")
    num3=input("[third number]+[enter]")
    opt=input("(1)GCD or (2) LCM+[enter]:")

    calculate(int(num1),int(num2),int(num3),int(opt))