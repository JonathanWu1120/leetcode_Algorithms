class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #zeroes = 0
        done = False
        var = len(nums) - 1
        #count = len(nums) - nums.count(0) -1
        while done == False:
            if len(nums) == 1:
                done = True
            if nums[var] != 0:
                var -= 1
            elif nums[var] == 0:
                #print(nums)
                nums.pop(var)
                nums.append(0)
                var -= 1
                #print(nums)
            if var == 0:
                if nums[var] == 0:
                    nums.pop(var)
                    nums.append(0)
                done = True