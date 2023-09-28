def power_x(x, n):
    # conditions initiales
    if n == 0:
        return 1
    elif n == 1:
        return x
    # Recursivité :
    else:
        return x * power_x(x, n - 1)

x = float(input("Enter a number : "))
n = int(input("Enter a whole number : "))
print(f"{x}^{n} = {power_x(x,n)}")


