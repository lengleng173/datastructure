class Solution:
    def trap(self, height: list[int]) -> int:
        highest=max(height)
        high_idx=height.index(highest)
        stack=[]
        sum=0
        for i in range(0,high_idx):
            if len(stack)>0 and height[i]>=height[stack[-1]]:
                stack.append(i)
            if len(stack)==0:stack.append(i)
        restack=[]        
        for i in range(len(height)-1,high_idx-1,-1):
            
            if len(restack)>0 and height[i]>=height[restack[-1]]:
                restack.append(i)
            if len(restack)==0:restack.append(i)
        for i in range(high_idx-1,0,-1):
            if i>stack[-1] :
                sum+=max(height[stack[-1]]-height[i],0)
            if i==stack[-1]:
                stack.pop()
        for i in range(high_idx,len(height)):
            if i<restack[-1]:
                sum+=max(height[restack[-1]]-height[i],0)
            if i==restack[-1]:
                restack.pop()
        return sum
    
so=Solution()
height = [4,2,0,3,2,5]
print(so.trap(height))

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
#         # 双指针
#         left, right = 0, len(height) - 1

#         water = left_max = right_max = 0 

#         while left < right:
#             if height[left] < height[right]:
#                 if height[left] > left_max:
#                     left_max = height[left]
#                 else:
#                     water += left_max - height[left]
#                     left +=1
#             else:
#                 if height[right] > right_max:
#                     right_max = height[right]
#                 else:
#                     water += right_max - height[right]
#                     right -=1
#         return water 