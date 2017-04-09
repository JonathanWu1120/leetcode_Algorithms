class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = {}
        if len(nums) <= 1:
            return False
        for i in nums:
            if i not in arr:
                arr[i] = 1
            elif i in arr:
                return True
        return False