class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        for i in range(len(timeSeries)):
            x = timeSeries[i]
            try:
                a = timeSeries[i+1]
                if x + duration > a:
                    total += a - x
                elif x + duration <= a:
                    total += duration
            except:
                total += duration
        return total