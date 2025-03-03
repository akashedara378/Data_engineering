def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Generate first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci_recursive(i), end=" ")


def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Generate first 10 Fibonacci numbers
fibonacci_iterative(10)
