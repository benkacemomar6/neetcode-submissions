class Solution:
    def maxArea(self, h: List[int]) -> int:
        i=len(h)-1
        j=0
        m=0
        while(i-j>=1):
            x=min(h[i],h[j])
            surf=x*(i-j)
            m=max(m,surf)
            if h[i]==x:
                i=i-1
            else:
                j=j+1
        return m




        