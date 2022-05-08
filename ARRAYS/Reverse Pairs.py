'''
493. Reverse Pairs
Hard

2808

180

Add to List

Share
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
 
'''

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        sorted_arr = []
        for i in range( len(nums)-1, -1, -1):
            x = nums[i]//2
            if( x == nums[i]/2 ):
                x -= 1
            
            insertion_index_of_number_less_than_half = bisect.bisect_right(sorted_arr, x)
            res += insertion_index_of_number_less_than_half
            insertion_index = bisect.bisect_left(sorted_arr, nums[i])
            sorted_arr.insert(insertion_index, nums[i])
        return res
