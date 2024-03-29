def is_prime(number):
    if number <= 1:
        return "Not Prime"
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"
user_number = int(input("Enter a number: "))

result = is_prime(user_number)

print("The number is:", result)
