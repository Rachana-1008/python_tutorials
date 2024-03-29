def addition(a,b):
    add=a+b
    return add
result = addition(10,20)
print("addition is:",result)

def multiplication(a,b):
    add=a*b
    return add
result = multiplication(10,20)
print("multiplication 10is:",result)

def power(base, exponent):
    result = base ** exponent
    return result
base_number = float(input("Enter the base number: "))
exp = float(input("Enter the exponent: "))
result = power(base_number, exp)
print(result)

def division(x, y):
        div = x / y
        return div
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator (non-zero): "))
result = division(numerator, denominator)
print("Division result is:", result)

def subtraction(a,b):
    sub = a-b
    return sub
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = subtraction(num1, num2)
print("Subtraction is:", result)





