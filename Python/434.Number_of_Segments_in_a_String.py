class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = 0
        word = False
        for i in s:
            if i != " ":
                word = True
            elif i == " ":
                if word == True:
                    x += 1
                    word = False
        if len(s) > 0 and word == True:
            return x+1
        return x