def can_split_evenly(prices):
    total = sum(prices)
    if total % 3 != 0:
        return False

    target = total // 3
    partial_sum = 0
    count = 0
    for price in prices:
        partial_sum += price
        if partial_sum == target:
            count += 1
            partial_sum = 0
        elif partial_sum > target:
            return False

    return count == 3


n = int(input())
for _ in range(n):
    prices = list(map(int, input().split()))
    if can_split_evenly(prices):
        print("Yes")
    else:
        print("No")
