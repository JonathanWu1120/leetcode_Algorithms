class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        a = s.strip().split(" ")
        return len(a[len(a)-1])