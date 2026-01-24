# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。

 

# 示例 1:

# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:

# 输入: s = "rat", t = "car"
# 输出: false
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        dic1=dict()
        for i in range(len(s)):
            dic1[i]=dic1.get(s[i],0)+1 
            dic1[i]=dic1.get(t[i],0)-1 
        for key,value in dic1.items():
            if value!=0:return False
        return True