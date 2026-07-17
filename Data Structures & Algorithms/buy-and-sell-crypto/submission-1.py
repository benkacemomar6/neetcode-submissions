class Solution:
    def maxProfit(self, p: List[int]) -> int:
        x=0
        best=0
        for i in range (1,len(p)):
            if p[x]>p[i]:
                x=i
            else:
                best= max(best,(p[i]-p[x]))
        return best


       