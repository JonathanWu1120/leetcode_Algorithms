class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        x = {}
        arr = sorted(nums)
        arr.reverse()
        for i in range(len(arr)):
            if i == 0:
                x[arr[i]] = "Gold Medal"
            elif i == 1:
                x[arr[i]] = "Silver Medal"
            elif i == 2:
                x[arr[i]] = "Bronze Medal"
            else:
                x[arr[i]] = i+1
        for i in range(len(nums)):
            nums[i] = str(x[nums[i]])
        return nums
