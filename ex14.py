def fib(n):
    if(n == 0 or n == 1):
        return n
    else:
        return fib(n-1)+fib(n-2)

for i in range(0,20):
    print(fib(i))
