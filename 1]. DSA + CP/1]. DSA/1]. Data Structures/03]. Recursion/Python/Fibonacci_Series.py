# To print the fibonacci series
#0 1 1 2 3 5 8

def fib(n):
    return n if n in [0, 1] else fib(n-2)+fib(n-1)
for i in range(6):
    print(fib(i), end = " ")
