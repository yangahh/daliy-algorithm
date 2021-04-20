# solution1
def get_len_of_str(str):
    n = len(str)
    if n == 0:
        return 0
    
    dp = [1] * (n + 1)
    for i in range(1, n):
        for j in range(i):
            if str[i] == str[j]:
                dp[i] = 1
                break
            else:
                dp[i] = dp[i - 1] + 1
    return max(dp)

# dynamic programing 기법으로 해결

# solution2
def get_len_of_str2(str):
    max_count = 1
    serial_str = []
    for a in str:
        if a not in serial_str:
            serial_str.append(a)
        else:
            serial_str = [a] # 초기화
            max_count = max(max_count, len(serial_str))

    max_count = max(max_count, len(serial_str))
    return max_count
            

