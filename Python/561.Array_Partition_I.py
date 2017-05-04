class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = 0
        for i,k in enumerate(nums):
            if i % 2 == 0:
                a += k
        return a