#calculator program


def add_num(a1,b1):
    return a1 + b1
    

def sub_num( a2, b2 ):
    if a2==b2:
        return 0        #DEFAULT STATEMENTS
    elif a2>b2:
        return a2-b2
    else:
        return b2-a2


def mul_num( a3, b3 ):
    return a3*b3


def div_num( a4, b4 ):
    if a4==b4:
        if a4==0:
            return "0/0 not possible"

        return 1

    elif a4>b4:
        if b4==0:
            return "divide by 0"

        return a4/b4

    else:
        if a4==0:
            return "divide by 0"

        return b4/a4


a = int(input("Enter a: "))
b = int(input("Enter b: "))


print(
    add_num(a,b),
    sub_num(a,b),
    mul_num(a,b),
    div_num(a,b)
)