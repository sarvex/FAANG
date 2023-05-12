# Calculating the factorial of an given argument "n"
# Mathematical formula:
# n! = 1.2.3...(n-2).(n-1).n
def factorial(n):
    return 1 if n <= 1 else n*factorial(n-1)

print(factorial(5))
# OUTPUT: 120
print(factorial(0))
# OUTPUT 1
print(factorial(1))
# OUTPUT:1
