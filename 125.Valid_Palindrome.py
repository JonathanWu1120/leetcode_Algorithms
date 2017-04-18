class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0,len(s)-1
        while j > i:
            while not s[i].isalnum() and j > i:
                i += 1
            while not s[j].isalnum() and j > i:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
            