class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split(' ')
        for idx,ss in enumerate(a):
            # print(ss)
            a[idx]=ss[::-1]
        return ' '.join(a)

    
so=Solution()
s = "Let's take LeetCode contest"
print(so.reverseWords(s))