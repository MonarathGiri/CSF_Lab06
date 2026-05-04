#iterative
def fact_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#recursive
def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_rec(n-1)

n = int(input("Enter number: "))
print("Iterative factorial =", fact_iter(n))
print("Recursive factorial =", fact_rec(n))