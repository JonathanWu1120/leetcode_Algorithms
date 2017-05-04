class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in findNums:
            greater = False
            if nums.index(i)+1 == len(nums):
                arr.append(-1)
            else:
                for j in range(nums.index(i),len(nums)):
                    #print(j,"j")
                    if nums[j] > i:
                        arr.append(nums[j])
                        greater = True
                        break
                if greater == False:
                    arr.append(-1)
                    #print(nums[j],nums.index(i),i)
        return arr
                