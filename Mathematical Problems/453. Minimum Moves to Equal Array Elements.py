class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum((nums[i-1]-nums[i])*i for i in range(1, len(nums)))
