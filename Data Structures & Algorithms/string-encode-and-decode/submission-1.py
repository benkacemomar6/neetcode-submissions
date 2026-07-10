class Solution:
    def summ(ch:str):
        
        return len(ch)


    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        s=""
        l=[]
        for ch in strs:
            s=s+ str(len(ch))
            s=s+','
        s=s+'Ĭ' 
        for ch in strs:
            s=s+ch   
            
        return s


    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        
        c= s[:s.find("Ĭ")]# toul
        print(c)
        
        x=s[s.find("Ĭ")+1:]# el klma
        print(x)
        l=""
        listt=[]
        w=0
        z=0
        for i in range(len(c)):
            if(c[i]!=','):
                l=l+c[i]
            else:
                d=int(c[w:i]) # toul el klma
                w=i+1
                listt.append(x[z:z+d])
                z=z+d
                l=""
                
        return listt



       
      
        





