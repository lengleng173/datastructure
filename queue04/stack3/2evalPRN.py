class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def caculate(x,y,operator):
            if operator=='+':
                return x+y
            if operator=='-':
                return x-y
            if operator=='*':
                return x*y
            if operator=='/':
                return int(x/y)
        stack=[]
        operator=['+','-','*','/']
        for i in tokens:
            if i in operator:
                y=stack.pop()
                x=stack.pop()
                stack.append(caculate(x,y,i))
            else:
                stack.append(int(i))
        return stack.pop()
    
so=Solution()
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(so.evalRPN(tokens))