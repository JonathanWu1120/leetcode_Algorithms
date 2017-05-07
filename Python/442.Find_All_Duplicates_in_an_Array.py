class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i,k in enumerate(nums):
            if nums[abs(k)-1] > 0:
                nums[abs(k)-1] *= -1
            elif nums[abs(k)-1] < 0:
                arr.append(abs(k))
                nums[abs(k)-1] *= -1
        return arr