def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    a=set()
    left=0
    current_len=0
    max_len=0
    for i in range(len(s)):
        while s[i] in a:
            a.remove(s[left])
            left+=1
            current_len-=1
        a.add(s[i])
        current_len+=1
        max_len=max(max_len,current_len)
    return max_len

s='pwwkew'
print(lengthOfLongestSubstring(s))
