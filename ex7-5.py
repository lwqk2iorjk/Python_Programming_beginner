def factorial(n):
    if n == 1:
        return 1
    else:
        print(n)
    return factorial(n - 1)

print(factorial(int(input("input num: "))))
