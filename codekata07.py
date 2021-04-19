# 과반수 이상
def more_than_half2(nums):
    for n in nums:
        if nums.count(n) > len(nums)/2:
            return n
        return "no"



def more_than_half(nums):
    
    element_cnt = {}
    for num in nums:
        if num not in element_cnt:
            element_cnt[num] = 1
        else:
            element_cnt[num] += 1
    
    maxmum_k = nums[0]
    maxmum_v = element_cnt[nums[0]]
    
    for k, v in element_cnt.items():
        if v > maxmum_v:
            maxmum_k = k
            maxmum_v = v
            
    return maxmum_k
