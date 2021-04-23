def get_prefix(strs):
    if strs == []:
        return ''

    min_len = 999999
    for str in strs:
        min_len = min(len(str), min_len)
    
    prefix = []
    for i in range(min_len):
        for j in range(1, len(strs)):
            if strs[j-1][i] != strs[j][i]:
                return "".join(prefix)
        prefix.append(strs[j][i])
    
    return "".join(prefix)


# solution (21.04.23)
def get_prefix(strs):
    if not strs:
        return ""
    
    min_len = min(list(map(len, strs)))
    result = []
    for i in range(min_len):
        for j in range(len(strs)):
            if j == 0:
                result.append(strs[j][i])

            if strs[j][i] != result[i]:
                result.pop()
                return "".join(result)

    return "".join(result)
