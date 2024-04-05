def main():
    n = int(input())
    word = input()
    width = 3 * n + 6
    height = 3 * n + 1

    for i in range(n):
        print(" " * n + "~ ~ ~")

    print("=" * (width - 1))

    middle = n // 2
    formula = (width - 3) - (n - 1) - len(word)

    for i in range(1, n - 1):
        if i == middle:
            print("|" + "~" * n + word.upper() + "~" * n + "|" + " " * (n - 1) + "|")
        else:
            print("|" + "~" * (n * 2 + 4) + "|" + " " * (n - 1) + "|")

    print("=" * (width - 1))

    newWidth = n * 2 + 6
    for i in range(n):
        print(" " * i + "\\" + "@" * (newWidth - 2 * i - 2) + "/")

    print("-" * (width - 1))


if __name__ == "__main__":
    main()
