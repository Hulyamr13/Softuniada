def main():
    n = int(input())
    for _ in range(n):
        nums = list(map(int, input().split()))
        print("Yes" if check_3_partitions(nums) else "No")

def check_3_partitions(nums):
    total_sum = sum(nums)
    if total_sum % 3 != 0:
        return False

    target_sum = total_sum // 3
    sum_reached = [[False] * (target_sum + 1) for _ in range(target_sum + 1)]
    sum_reached[0][0] = True

    for num in nums:
        for s1 in range(target_sum, -1, -1):
            for s2 in range(target_sum, -1, -1):
                if sum_reached[s1][s2]:
                    if s1 + num <= target_sum and not sum_reached[s1 + num][s2]:
                        sum_reached[s1 + num][s2] = True
                    if s2 + num <= target_sum and not sum_reached[s1][s2 + num]:
                        sum_reached[s1][s2 + num] = True

    return sum_reached[target_sum][target_sum]

if __name__ == "__main__":
    main()