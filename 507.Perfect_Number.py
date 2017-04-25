from math import sqrt
class Solution(object):
    def factors(self,num):
        arr = []
        for i in range (1,int(sqrt(num))+2):
            if num%i == 0 and i not in arr:
                arr.append(i)
                if i != 1 and (num/i) not in arr:
                    arr.append(num/i)
        return arr
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 6:
            return False
        factors = self.factors(num)
        return sum(factors) == num