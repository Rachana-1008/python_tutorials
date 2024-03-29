#lambda arguments : Expression

add = lambda x,y : x+y
print(add(10,20))

str =input("enter a string")
string= lambda string : string.split()
print(string(str))

number =int(input("enter a number"))
odd_even = lambda : "is a even number" if number %2==0 else "is a add number"
print(odd_even())


year = int(input("Enter a year: "))
leap = lambda: "is a leap year" if year % 4 == 0 and year % 100 != 0 else "is not a leap year"
print(leap())


str =input("enter a string")
string= lambda string : string.upper()
print(string(str))

str =input("enter a string")
string= lambda string : string.lower()
print(string(str))

str =input("enter a string")
string= lambda string : string.split()
print(string(str))