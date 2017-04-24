class Solution(object):
    def findNum(self,nums,target):
        low = 0
        high = len(nums)
        # try:
        while low + 1 < high:
            test = (low+high)/2
            if nums[test] > target:
                high = test
            else:
                low = test
        # except IndexError:
        if nums[low] == target:
            return low
        return -1
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = len(nums)
        if a == 1 and nums[0] == target:
            return [0,0]
        elif a == 0 or a == 1 or target < nums[0] or target > nums[a-1]:
            return [-1,-1]
        isin = self.findNum(nums,target)
        if isin >= 0:
            start = end = isin
            try:
                while nums[start] == target and start >= 0:
                    start -= 1
            except IndexError:
                pass
            try:
                while nums[end] == target and end < a:
                    end += 1
            except IndexError:
                pass
            return start+1,end-1
        return [-1,-1]