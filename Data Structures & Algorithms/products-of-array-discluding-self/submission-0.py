class Solution:
    def productExceptSelf(self, x: List[int]) -> List[int]:
        l=[1]*(len(x))
        pref=1
        for i in range (len(x)):
            l[i]=pref
            pref=pref*x[i]
            
        
        suff=1
        for i in range(len(x)-1,-1,-1):
            l[i]=l[i]*suff
            suff=suff*x[i]
        return l