class Solution:
    def evalRPN(self, t: List[str]) -> int:
        
        n=[]
        
        for i in range(len(t)):
            if (t[i] not in ["+","-","/","*"] ):
                z=int(t[i])
                n.append(z)
            else:
                x=n.pop()
                y=n.pop()
                if t[i]=="+":
                    n.append(x+y)
                    

                
                elif t[i]=="-":
                    n.append(y-x)

                elif t[i]=="*":
                    n.append(x*y)
                
                elif t[i]=="/":
                     n.append(int(y/x))
        return n.pop()
                
                    
                
            


            

        