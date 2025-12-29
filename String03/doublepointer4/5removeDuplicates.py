# 给出由小写字母组成的字符串 s，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

# 在 s 上反复执行重复项删除操作，直到无法继续删除。

# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

# 输入："abbaca"
# 输出："ca"

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
       # 转换为列表便于操作
        chars = list(s)
        i = 0
        
        while i < len(chars) - 1:
            if chars[i] == chars[i + 1]:
                # 删除相邻的两个相同字符
                del chars[i:i + 2]
                # 如果删除后前面还有字符，需要回退一步检查
                if i > 0:
                    i -= 1
            else:
                i += 1
        
        return ''.join(chars)
    
so=Solution()
s = "xrjjjjjrp"
print(so.removeDuplicates(s))