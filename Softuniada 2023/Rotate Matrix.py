def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

rotate(matrix)
print_matrix(matrix)
