class Solution(object):
    def minMoves(self, nums):
        fact = min(nums)
        rounds = 0
        for i in nums:
            rounds += i - fact
        return rounds
            