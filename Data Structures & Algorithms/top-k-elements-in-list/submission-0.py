class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num={}
        l=[]
        for n in nums:
            num[n]=num.get(n,0)+1
        sorted_freq = sorted(num.items(), key=lambda x: x[1],reverse=True)


        l=[]

        for i in range(k):
            l.append(sorted_freq[i][0])
        return l