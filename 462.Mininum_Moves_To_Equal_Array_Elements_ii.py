class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        middle = nums[len(nums)//2]
        total = 0
        for i in nums:
            total += abs(i-middle)
        return total
        #difference of all numbers with median