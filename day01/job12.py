# Job 1.2 :

def draw_triangle(n):
    if n < 2:
        print("Error, n must be at least 2.")
        return

    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        if i == 1:
            print(spaces + '/'+ '\\')
        elif i == n:
            print('/' + '_' * (2 * n - 2) + '\\')
        else:
            print(spaces + '/' + ' ' * (2 * i - 2) + '\\')

# Test :
draw_triangle(6)