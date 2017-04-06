class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            track = 0
            for i in str(num):
                track += int(i)
            num = track
        return num
        