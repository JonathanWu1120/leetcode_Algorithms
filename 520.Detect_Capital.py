class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cap = 0
        for c in word:
            if c.isupper():
                cap += 1
        if cap == len(word):
            return True
        elif word[0].isupper() and cap == 1:
            return True
        elif cap == 1 and not word[0].isupper():
            return False
        elif word[0].isupper() and cap > 1:
            return False
        elif cap > 1:
            return False
        elif cap == 0:
            return True