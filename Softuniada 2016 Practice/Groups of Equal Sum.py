numbers = [int(input()) for _ in range(4)]

total_sum = sum(numbers)

if total_sum % 2 == 0:
    target_sum = total_sum // 2

    possible_sums = set()

    possible_sums.add(0)

    for num in numbers:
        temp_sums = set()

        for prev_sum in possible_sums:
            new_sum = prev_sum + num
            temp_sums.add(new_sum)

        possible_sums.update(temp_sums)

    if target_sum in possible_sums:
        print("Yes")
        print(target_sum)
    else:
        print("No")
else:
    print("No")
