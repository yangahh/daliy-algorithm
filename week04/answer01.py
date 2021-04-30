# solution1
def solution(N):
    bin_n = bin(N)[2:]
    dp = [0] * len(bin_n)
    max_cnt = 0
    for i in range(1, len(bin_n)):
        if bin_n[i] == '1':
            dp[i] = 0
            if dp[i-1] > max_cnt:
                max_cnt = dp[i-1] 
        else:
            dp[i] = dp[i-1] + 1

    return max_cnt
