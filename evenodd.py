def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

user_number = int(input("Enter a number: "))

result = check_even_odd(user_number)

print("The number is:", result)
