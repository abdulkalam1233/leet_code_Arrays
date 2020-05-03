class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        for i,v in enumerate(nums):
            if(v != 0 and i !=0):
                nums[i] += nums[i-1]
        return max(nums)
        
