def factorial(n):
    # conditions initiales
    if n == 0 or n == 1:
        return 1
    # Recursivité
    else:
        return n * factorial(n - 1)

#test :
n=3
print(factorial(n))
