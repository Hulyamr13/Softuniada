n = int(input())
array = list(map(int, input().split()))

for i in range(1, n, 2):
    if array[i] > array[i - 1]:
        array[i], array[i - 1] = array[i - 1], array[i]

for i in range(2, n, 2):
    if array[i] < array[i - 1]:
        array[i], array[i - 1] = array[i - 1], array[i]

print(*array)
