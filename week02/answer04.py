def top_k(nums, k):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    sort_dic_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    result = []
    for kv in sort_dic_list:
        result.append(kv[0])
    result = result[:k]

    return result

# solution2 (21.04.25)
def top_k(nums, k):
    cnt_dict = {}
    for num in nums:
        if cnt_dict.get(num):
            cnt_dict[num] += 1
        else:
            cnt_dict[num] = 1

    sorted_nums = sorted(cnt_dict.items(), key = lambda x: x[1], reverse=True)
    return [sorted_nums[i][0] for i in range(k)]
