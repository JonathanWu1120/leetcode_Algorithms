class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        a,b,x = len(nums),len(nums[0]),0
        if a * b != r * c:
            return nums
        arr,arr2 = [j for i in nums for j in i],[]
        l = len(arr)
        if r == 1 and (a == r and c == b):
            arr2.append(arr)
            return arr2
        while x < l:
            arr2.append(arr[x:x+c])
            x += c
        return arr2
        