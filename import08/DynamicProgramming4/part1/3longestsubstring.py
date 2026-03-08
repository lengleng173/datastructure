
#dp[i][j] 表示从 i 到 j 的子串是否为回文
def longestPalindrome( s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    
    # dp[i][j] 表示 s[i:j+1] 是否为回文
    dp = [[False] * n for _ in range(n)]
    
    # 初始化：所有单个字符都是回文
    for i in range(n):
        dp[i][i] = True
    
    start = 0  # 最长回文子串的起始位置
    max_len = 1  # 最长回文子串的长度
    
    # 检查长度为2的子串
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2
    
    # 检查长度≥3的子串
    for length in range(3, n+1):  # 子串长度
        for i in range(n-length+1):  # 起始位置
            j = i + length - 1  # 结束位置
            
            # 状态转移：首尾字符相等且中间部分是回文
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
    
    return s[start:start+max_len]

print(longestPalindrome("cbbd"))