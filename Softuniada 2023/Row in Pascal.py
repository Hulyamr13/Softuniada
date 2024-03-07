def calculate_pascal_row(n):
    row = [1]
    for i in range(1, n + 1):
        row.append(row[i - 1] * (n - i + 1) // i)
    return row


def main():
    n = int(input())
    row = calculate_pascal_row(n)
    print(*row)


if __name__ == "__main__":
    main()
