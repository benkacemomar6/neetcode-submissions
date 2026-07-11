class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        l=[nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                l.append(nums[i])
        max=0
        s=0
        print(l)
        for i in range(1, len(l)):
            if l[i] == l[i-1] + 1:
                s += 1
            else:
                if s > max:
                    max = s
                s = 0

        if s > max:
            max = s
                
                
        return max+1




        