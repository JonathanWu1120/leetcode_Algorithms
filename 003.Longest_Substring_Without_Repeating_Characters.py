class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos,m,beg,cur = {},0,0,-1
        for cur in range(len(s)):
            #if the character is in the dictionary, and the value is bigger than the previous position, replace that position with one plus the current one
            if s[cur] in pos and pos[s[cur]] >= beg:
                beg = pos[s[cur]] + 1
            #if it isnt, the max is now the higher value between the current max and the difference in position between the current value and the last recorded unique character
            else:
                m = max(m, cur - beg + 1)
            pos[s[cur]] = cur
        return m