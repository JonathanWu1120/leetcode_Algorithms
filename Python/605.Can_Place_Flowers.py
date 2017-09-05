class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        new_f = 0
        if flowerbed[0] == 0:
            track = 1
        else:
            track = 0
        for i,j in enumerate(flowerbed):
            if j == 0:
                track += 1
            elif j == 1:
                track = 0
            if track == 2:
                try:
                    if flowerbed[i+1] == 0:
                        new_f += 1
                        track = 0
                    elif flowerbed[i+1] == 1:
                        track = 0
                except:
                    new_f += 1
                    track = 0
        return new_f >= n