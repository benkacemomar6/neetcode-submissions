class Solution:
    def maxSlidingWindow(self, n: List[int], k: int) -> List[int]:
        l=[]
        m=max(n[0:k])
        mm=m
        for i in range(k,len(n)):
            mm=max(n[i-k:i])
            l.append(mm)
        l.append(max(n[len(n)-k:]))
        
        return l
            

