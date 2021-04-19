# def two_sum(nums, target):
#   for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#       if nums[i] + nums[j] == target:
#         return [i, j]

def two_sum(nums, target):
  len_nums = len(nums)
  for i in range(len_nums):
    for j in range(i):
      print(f'i: {i}')
      print(f'j: {j}')
      if nums[i] + nums[j] == target:
        print([i, j])