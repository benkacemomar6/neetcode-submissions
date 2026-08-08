class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'}
        if len(s)==1:
            return False
        for i in range(len(s)):
            if (s[i] not in pairs):
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                    
                z=st.pop()
                if (pairs[s[i]] != z):
                    return False
        if len(st)>0:
            return False
        return True







       
        




        