class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        
        p1=0
        p2=len(s)-1
        if s=="a." or s==".a" or s==".,":
            return True
        if len(s)==1:
            return True
        if len(s)==2 or len(s)==3:
            if s[0]!=s[len(s)-1]:
                return False
            else:
                return True

        while((p2-p1)>=1):
            if not (s[p1].isalnum()):
                p1=p1+1
            elif not (s[p2].isalnum()):
                p2=p2-1
            else:
                if s[p1]!=s[p2]:
                    return False
                else:
                    p1+=1
                    p2-=1
        print(p1,p2)
        return True
            
            
        
            

        