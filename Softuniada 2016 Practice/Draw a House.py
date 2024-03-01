n = int(input())

for line in range(1, n):
    if line == 1:
        print('.' * (n - line) + '*' + '.' * (n - line))
    else:
        print('.' * (n - line) + '*' + ' ' * (2 * line - 3) + '*' + '.' * (n - line))

print('* ' * n)

print('+' + '-' * (2 * n - 3) + '+')
for _ in range(n - 2):
    print('|' + ' ' * (2 * n - 3) + '|')
print('+' + '-' * (2 * n - 3) + '+')
