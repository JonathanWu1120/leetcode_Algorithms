class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                arr.append(i)
        return arr