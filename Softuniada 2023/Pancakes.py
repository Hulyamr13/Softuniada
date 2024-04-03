def kadane(input_list):
    max_sum = float('-inf')
    current_sum = 0
    start_index = 0
    end_index = 0
    max_start = 0
    max_end = 0

    for i in range(len(input_list)):
        if current_sum < 0:
            start_index = i
            end_index = i
            current_sum = 0

        current_sum += input_list[i]
        end_index = i

        if current_sum > max_sum:
            max_start = start_index
            max_end = end_index
            max_sum = current_sum
        elif current_sum == max_sum and (end_index - start_index) > (max_end - max_start):
            max_start = start_index
            max_end = end_index

    return max_sum, max_start, max_end


input_list = list(map(int, input().split()))
max_sum, max_start, max_end = kadane(input_list)
print(max_sum, max_start, max_end)
