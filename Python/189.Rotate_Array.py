class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            while k > len(nums):
                k -= len(nums)
            arr = []
            for i in range(k):
                arr.append(nums.pop())
            for i in range(k):
                nums.insert(i,arr.pop())