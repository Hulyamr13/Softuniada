def solve(n, index, whiteIndex, blackIndex, dp, elements):
    if index == n:
        return 0

    if dp[index][whiteIndex][blackIndex] != 0:
        return dp[index][whiteIndex][blackIndex]

    secondaryState = 0
    tertiaryState = 0

    if whiteIndex == n or elements[index] > elements[whiteIndex]:
        secondaryState = 1 + solve(n, index + 1, index, blackIndex, dp, elements)

    if blackIndex == n or elements[index] < elements[blackIndex]:
        tertiaryState = 1 + solve(n, index + 1, whiteIndex, index, dp, elements)

    dp[index][whiteIndex][blackIndex] = max(solve(n, index + 1, whiteIndex, blackIndex, dp, elements), secondaryState, tertiaryState)

    return dp[index][whiteIndex][blackIndex]


if __name__ == "__main__":
    n = int(input())

    dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    elements = list(map(int, input().split()))

    print(n - solve(n, 0, n, n, dp, elements))
