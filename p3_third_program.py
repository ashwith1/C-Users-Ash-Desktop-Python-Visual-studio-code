#function def
#function name
#passing arguments
#function only executes when called
def add_num(a,b): # : -> continutity operator
    print("Inside add function",a,b)
    return a + b
 #   pass #do nothing


a = int(input("Enter a : "))
b = int(input("Enter b : "))


print(add_num(a,b)) # values are sent
print(add_num(int(input("Enter a1 : ")), int(input("Enter b1 : "))))
print(add_num(2,3))
#code is reusable

def add(a1,b1):
    pass

print(add_num("abc" , "def"))
print(add_num(2,3))
print(add_num([2,3],['abc','def']))

