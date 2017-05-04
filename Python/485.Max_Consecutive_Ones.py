class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        count = 0
        for i in nums:
            if i == 1: #and nums.index(i) != len(nums)-1:
                count += 1
                if count > max:
                    max = count
            else:
                count = 0
        return max
                
                