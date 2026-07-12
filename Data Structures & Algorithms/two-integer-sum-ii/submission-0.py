class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        i=0
        j=(len(n)-1)
        while(j-i>=1):
            if((n[i]+n[j])==target):
                return ([i+1,j+1])
            elif(n[i]+n[j]<target):
                i=i+1
            else:
                j=j-1


