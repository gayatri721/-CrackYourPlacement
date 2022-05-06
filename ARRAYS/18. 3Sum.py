# https://www.youtube.com/watch?v=onLoX6Nhvmg&ab_channel=takeUforward
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            h = len(nums)-1
            while l<h:
                if (nums[i]+nums[l]+nums[h])==0:
                    res.add((nums[i], nums[l], nums[h]))
                    l += 1
                    while nums[l]==nums[l-1] and l<h:
                        l += 1
                elif (nums[i]+nums[l]+nums[h])<0:
                    l += 1
                else:
                    h -= 1
        return res
        
