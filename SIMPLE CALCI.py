import math
print("\t-----calculator-----")
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if a>b:
        a-=b
        return a
    else:
        b-=a
        return b

def mul(a,b):
    a*=b
    return a
def div(a,b):
    q = a/b
    r= a%b
    print("the quotient is : %s"%q)
    print('the remainder is :%s'%r)

while(True):
    print("\n\n Choose the operation you want to perform")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.EXIT")

    choice = int(input("enter your choice: "))

    if choice==1:
        print("\n\n enter two numbers:")
        num1 = int(input())
        num2 = int(input())
        s = sum(num1,num2)
        print("the sum is %s:"%s)

    elif choice==2:
        print("\n\n enter two numbers:")
        num1 = int(input())
        num2 = int(input())
        m = sub(num1,num2)
        print("the sum is %s:"%m)

    elif choice == 3:
        print("\n\n enter two numbers:")
        num1 = int(input())
        num2 = int(input())
        p = mul(num1, num2)
        print("the sum is %s:" %p)

    elif choice == 4:
        print("\n\n enter two numbers:")
        num1 = int(input())
        num2 = int(input())
        div(num1, num2)

    else:
        print("\nyou choose to exit.Bye..")
        break