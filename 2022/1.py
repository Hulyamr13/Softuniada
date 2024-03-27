def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def find_lcm(x, y):
    gcd = find_gcd(x, y)
    lcm = (x * y) // gcd
    return lcm


N = int(input())
M = int(input())

gcd = find_gcd(N, M)
lcm = find_lcm(N, M)

print(gcd + lcm)
