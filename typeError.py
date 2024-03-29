'''a=int(input("Enter a Number"))
b=input("Enter Second Number")
c=a/b
print("Division is",c)'''

try:
    a=int(input("Enter a Number"))
    b=input("Enter Second number")
    c=a/b
    print("Division is ",c)
except:
    print("Type error occured")