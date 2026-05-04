# Iterative
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Recursive with call counter
count = 0
def fib_rec(n):
    global count
    count += 1
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

n = int(input("Enter n: "))

print("Iterative Fibonacci:", fib_iter(n))

count = 0
print("Recursive Fibonacci:", fib_rec(n))
print("Recursive calls:", count)