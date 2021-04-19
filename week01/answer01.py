# solution1
def two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# solution2
def two_sum(nums, target):
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [j, i]
