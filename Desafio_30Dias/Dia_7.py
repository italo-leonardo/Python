def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

T = int(input())

for _ in range(T):
    N = int(input())
    resultado = fibonacci(N)
    print(f'Fib({N}) = {resultado}')