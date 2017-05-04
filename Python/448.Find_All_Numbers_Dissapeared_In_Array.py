class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = {i:0 for i in range(1,len(nums)+1)}
        arr = []
        for i in nums:
            a[i] = 1
        for i,j in a.items():
            if j == 0:
                arr.append(i)
        return arr