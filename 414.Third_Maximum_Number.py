class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return float("-inf")
        high = float("-inf")
        high2 = float("-inf")
        high3 = float("-inf")
        for i in nums:
            if i > high:
                high3 = high2
                high2 = high
                high = i
            elif i > high2 and i < high:
                high3 = high2
                high2 = i
            elif i > high3 and i < high2:
                high3 = i
        if high3 == float("-inf"):
            return high
        return high3