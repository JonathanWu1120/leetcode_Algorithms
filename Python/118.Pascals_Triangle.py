class Solution(object):
    def factorial(self,num):
        total = 1
        for i in range(1,num+1):
            total *= i
        return total
    def nth_row(self,num):
        arr = []
        fac = self.factorial(num)
        for i in range(num+1):
            if i == 0 or i == num:
                arr.append(1)
            else:
                arr.append(fac/(self.factorial(i)*(self.factorial    (num-i))))
        return arr
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(numRows):
            arr.append(self.nth_row(i))
        return arr