def largest_number(nums):
    arr = [str(num) for num in nums]

    arr.sort(key=lambda x: (x * 4)[:4], reverse=True)

    result = ''.join(arr)

    while result[0] == '0' and len(result) > 1:
        result = result[1:]

    return result


numbers = list(map(int, input().split()))
print(largest_number(numbers))
