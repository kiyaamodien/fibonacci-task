# for nth Fibonacci number
x = int(input("enter a number"))


def fibonacci(n):
    if n < 0:
        print("wrong input")
    elif n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


for i in range(x):
    print(fibonacci(i))
