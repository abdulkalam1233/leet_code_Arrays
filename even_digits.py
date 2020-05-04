class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if math.ceil(math.log10(num + 1)) % 2 == 0:
                result += 1
        return result
        
