class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        stack=[]
        m=0
        for i,h in enumerate(nums):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                m=max(m,(height*(i-index)))
                start=index
            stack.append((start,h))
        for i,h in stack:
            m=max(m,(h*(len(nums)-i)))
        return m
            

        