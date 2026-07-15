class Solution:
    def trap(self, h: List[int]) -> int:
        x=0
        y=1
        d=0
        
        surf=0
        m=max(h)
        z=h.index(m)
        while(y<=z):
            if h[x]>h[y]:
                y=y+1

            else:
                d=y-x-1
                surf+=(min(h[x],h[y])*d)
                for i in range(x+1,y):
                    surf=surf-h[i]
                x=y
                y=x+1
        
        x=len(h)-1
        y=len(h)-2
        d=0
        while(y>=z):
            if h[x]>h[y]:
                y=y-1

            else:
                d=x-y-1
                surf+=(min(h[x],h[y])*d)
                for i in range(y+1,x):
                    surf=surf-h[i]
                x=y
                y=x-1
        

        
        return surf





            

        