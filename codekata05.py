# 문자열들이 담긴 리스트를 받아서 공통된 시작 단어(prefix)를 반환

def get_prefix(strs):
    if strs == []:
        return ''

    # 가장 짧은 문자열의 길이 구하기
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
