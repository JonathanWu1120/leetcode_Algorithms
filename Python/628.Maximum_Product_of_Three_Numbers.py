class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums) -1
        nums.sort()
        possible_negative = nums[0]
        possible_negative_2 = nums[1]
        biggest = nums[a]
        biggest_2 = nums[a-1]
        biggest_3 = nums[a-2]
        if possible_negative * possible_negative_2 > biggest_2*biggest or possible_negative * possible_negative_2 > biggest_2 * biggest_3:
            return possible_negative*possible_negative_2*biggest 
        return biggest*biggest_2*biggest_3