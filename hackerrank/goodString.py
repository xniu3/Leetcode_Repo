def goodString(min_length, max_length, one_group, zero_group):
    dp = [0] * (max_length + 1)
    dp[0] = 1
    for i in range(1, max_length + 1):
        if i >= one_group:
            dp[i] += dp[i - one_group]
        if i >= zero_group:
            dp[i] += dp[i - zero_group]
    print(dp)
    return sum(dp[min_length:max_length + 1])

result = goodString(1,3, 2,1)
print("result is", result)
