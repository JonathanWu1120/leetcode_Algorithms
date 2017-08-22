class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        a = []
        min_sum = float("inf")
        for i,j in enumerate(list1):
            for k,l in enumerate(list2):
                if j == l:
                    if i+k < min_sum:
                        min_sum = i+k
                        a = []
                        a.append(j)
                        repeat = False
                    elif i+k == min_sum:
                        a.append(j)
                        repeat = True
        if repeat == True:
            a.reverse()
        return a