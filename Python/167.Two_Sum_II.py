class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        b = len(numbers) - 1
        c = True
        while c:
            if numbers[a] + numbers[b] > target:
                b -= 1
            elif numbers[a] + numbers[b] < target:
                a += 1
            elif numbers[a] + numbers[b] == target:
                return [a+1,b+1]