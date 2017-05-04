class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        for i in range(1,n+1):
            if i%3==0:
                if i%5==0:
                    arr.append("FizzBuzz")
                else:
                    arr.append("Fizz")
            elif i%5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i))
        return arr