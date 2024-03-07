nums = list(map(int, input().split()))

if nums[0] + nums[1] + nums[2] == 13 or \
   nums[0] + nums[1] - nums[2] == 13 or \
   nums[0] - nums[1] + nums[2] == 13 or \
   nums[0] - nums[1] - nums[2] == 13 or \
   -nums[0] + nums[1] + nums[2] == 13 or \
   -nums[0] + nums[1] - nums[2] == 13 or \
   -nums[0] - nums[1] + nums[2] == 13 or \
   -nums[0] - nums[1] - nums[2] == 13:
    print("Yes")
else:
    print("No")
