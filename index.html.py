n = 5
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(1, n):
    for j in range(n):
        if j == 0 or j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print('----------------------------------')


n = 5
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or (i == j and j <= n // 2) or (i + j == n - 1 and j >= n // 2):
            print('*', end='')
        else:
            print(' ', end='')
    print()
