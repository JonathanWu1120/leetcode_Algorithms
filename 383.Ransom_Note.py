class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        is_in = True
        arr = []
        for c in magazine:
            arr.append(c)
        for c in ransomNote:
            is_in = is_in and (c in arr)
            if is_in == False:
                break
            else:
                arr.remove(c)
        return is_in
            