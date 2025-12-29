# 387给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

 

# 示例 1：

# 输入: s = "leetcode"
# 输出: 0
# 示例 2:

# 输入: s = "loveleetcode"
# 输出: 2

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=dict()
        for ss in s:
            a[ss]=a.get(ss,0)+1
        for idx,ss in enumerate(s):
            if a[ss]==1:
                return idx
            
        return -1