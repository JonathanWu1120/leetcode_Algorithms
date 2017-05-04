from math import sqrt
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        arr = []
        arr2 = []
        for i in range(1,int(sqrt(area))+2):
            if area%i == 0:
                arr.append(i)
                arr.append(area/i)
        a = arr[len(arr)-1]
        b = arr[len(arr)-2]
        if a>b:
            return a,b
        else:
            return b,a