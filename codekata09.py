def top_k(nums, k):
    dic = {}
    # for num in nums:
    #     if num not in dic:
    #         dic[num] = 1
    #     else:
    #         dic[num] += 1
    for num in nums:
        dic[num] = nums.count(num)

    print(dic.items())

    sort_dic_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    return [sort_dic_list[i][0] for i in range(k)]

    # result = []
    # for kv in sort_dic_list:
    #     result.append(kv[0])
    # result = result[:k]

    # return result


print(top_k([1, 1, 2, 2, 2, 2, 3, 3, 3], 2))
