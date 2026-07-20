class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l={}
        k=-1
        c=0
        m=0
        for i in range(len(s)):
            l[s[i]] = l.get(s[i], 0) + 1
            c=c+1
            if(l[s[i]]>1):
                while(l[s[i]]>1):
                    k=k+1
                    l[s[k]] = l.get(s[k], 0) - 1
                    c=c-1
            
                
            m=max(m,c)
        return m
                
            


            
            

        