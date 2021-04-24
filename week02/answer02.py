# solution1
#def more_than_half(nums):
#    
#    element_cnt = {}
#    for num in nums:
#        if num not in element_cnt:
#            element_cnt[num] = 1
#        else:
#            element_cnt[num] += 1
#    
#    maximum_k = nums[0]
#    maximum_v = element_cnt[nums[0]]
#    
#    for k, v in element_cnt.items():
#        if v > maximum_v:
#            maximum_k = k
#            maximum_v = v
#            
#    return maximum_k


#solution2 (21.04.25)
def more_than_half(nums):
    len_nums = len(nums)
    cnt_dict = {}
    for num in nums:
        if cnt_dict.get(num):
            cnt_dict[num] += 1
        else:
            cnt_dict[num] = 1

    for k, v in cnt_dict.items():
        if v > len_nums/2:
            return k

