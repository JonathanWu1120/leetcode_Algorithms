class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)),len(candies)/2)
        # unique = len(set(candies))
        # size = len(candies)/2
        # if unique > size:
        #     return size
        # return unique