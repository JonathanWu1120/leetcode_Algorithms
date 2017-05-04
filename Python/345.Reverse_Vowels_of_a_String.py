class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = ["a",'e','i','o',"u",'A','E',"O","I","U"]
        k = list(s)
        i = 0
        j = len(s) - 1
        while j > i:
            while k[i] not in v and i < j:
                i += 1
            while k[j] not in v and j > i:
                j -= 1
            k[i],k[j] = k[j],k[i]
            i += 1
            j -= 1
        return "".join(k)