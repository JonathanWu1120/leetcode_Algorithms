class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up = 0
        left = 0
        for i in moves:
            if i == "U":
                up += 1
            elif i == "D":
                up -= 1
            elif i == "L":
                left += 1
            elif i == "R":
                left -= 1
        return up == 0 and left == 0