class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        j = 0
        k = 0
        x = False
        for i in range(len(nums)):
            if nums[i] == val:
                if x == False:
                    j = i
                    k = i
                    x = True
                k += 1
        del nums[j:k]
        return len(nums)