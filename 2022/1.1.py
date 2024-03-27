import math

N = int(input())
M = int(input())

print(math.gcd(N, M) + (N * M) // math.gcd(N, M))
