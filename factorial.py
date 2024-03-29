def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
user_number = int(input("Enter a number: "))
result = factorial(user_number)
print(f"The factorial of {user_number} is:", result)
