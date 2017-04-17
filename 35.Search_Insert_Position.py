class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        track = 0
        for i in range(len(nums)):
            if nums[i] < target:
                track = i+1
        return track