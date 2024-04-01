def spiral_order(matrix):
    result = []
    while matrix:
        result.extend(matrix.pop(0))

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        if matrix:
            result.extend(matrix.pop()[::-1])

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result

R = int(input())
C = int(input())
matrix = [list(map(int, input().split())) for _ in range(R)]

print(*spiral_order(matrix))
