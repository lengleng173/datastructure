class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left=['(','{','[']
        right=[')','}',']']
        stack=[]
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if len(stack)==0:
                    return False
                x=stack.pop()
                if left.index(x)!=right.index(i):
                    return False
        if len(stack)==0:return True
        else:return False

        # if len(s)%2 ==1:
        #     return False
        # pairs = {
        #     ')' : '(',
        #     '}' : '{',
        #     ']' : '['
        # }
        # stack = []
        # for c in s:
        #     if c in pairs:
        #         if stack and stack[-1] == pairs[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        # return len(stack) == 0