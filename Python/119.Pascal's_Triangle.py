class Solution(object):
    def factorial(self,num):
        total = 1
        for i in range(1,num+1):
            total *= i
        return total
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        arr = []
        fac = self.factorial(rowIndex)
        for i in range(rowIndex+1):
            arr.append(fac/(self.factorial(i)*(self.factorial(rowIndex-i))))
        return arr