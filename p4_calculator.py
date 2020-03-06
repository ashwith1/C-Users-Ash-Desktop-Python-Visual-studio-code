#replace something withcode

def add_num(a1,b1):
    print("add",a1,b1)
    return a1+b1
    

def sub_num(a2,b2):
    print("sub",a2,b2)
    return a2-b2
    

def mul_num(a3,b3):
    print("mul",a3,b3)
    return a3*b3
    

def div_num(a4,b4):
    print("div",a4,b4)
    return a4/b4
    

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(
    add_num(a,b),
    sub_num(a,b),
    mul_num(a,b),
    div_num(a,b)
)