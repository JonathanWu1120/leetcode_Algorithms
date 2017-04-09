class Solution(object):
    def missingNumber(self,nums):
        x = len(nums)
        nums.sort()
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        for i in range(x):
            if nums[i] != i:
                return i
        return x