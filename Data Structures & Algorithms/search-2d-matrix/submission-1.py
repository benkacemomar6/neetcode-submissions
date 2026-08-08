class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        nb=len(m)-1
        nt=0
        while(nb>=nt):
            mid=(nb+nt)//2
            if m[mid][0]==target:
                return True
            elif m[mid][0]<=target:
                nt=mid+1
            else:
                nb=mid-1
        r=len(m[nb])-1
        l=0
        print( nb)
        while l<=r:
            mid1=(l+r)//2
            if(m[nb][mid1]==target):
                return True
            elif m[nb][mid1]<target:
                l=mid1+1
            else:
                r=mid1-1
        return False





            







        