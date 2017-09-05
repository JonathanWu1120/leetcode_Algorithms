class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a,b = 0,0
        for i,j in enumerate(nums):
            index = abs(j)-1
            if j < 0:
                a = abs(j)
            nums[index] = -abs(j)
        for i,j in enumerate(nums):
            if j > 0:
                b = i+1
                break
        return a,b