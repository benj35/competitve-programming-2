class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum = 0
        for j in range(len(nums)):
            largest = smallest = nums[j]
            for i in range(j, len(nums)):
                largest = max(largest, nums[i])
                smallest = min(smallest, nums[i])
                sum += largest - smallest
        
        return sum
            