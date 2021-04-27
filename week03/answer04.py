def move_zeroes(nums):
    i = 0
    for _ in range(len(nums)):  # 리스트 길이만큼만 반복
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            i -= 1
        i += 1

    return nums
